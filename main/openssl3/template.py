pkgname = "openssl3"
pkgver = "3.4.1"
pkgrel = 1
build_style = "configure"
configure_script = "Configure"
configure_args = [
    "--prefix=/usr",
    "--openssldir=/etc/ssl",
    "--libdir=lib",
    "enable-ktls",
    "shared",
    "-Wa,--noexecstack",
]
make_install_args = ["MANSUFFIX=ssl"]
make_check_target = "test"
make_check_args = [
    "TESTS="
    # XXX: with ktls enabled this fails if the running env can't utilise it
    + "-test_afalg"
    # FIXME: broken now for some reason and the test server hangs
    + " -test_quic*"
    # flaky on ppc64le
    + " -test_key_share"
    + " -test_sslrecords"
    + " -test_sslsigalgs"
]
hostmakedepends = ["pkgconf", "perl"]
provides = [self.with_pkgver("openssl")]
pkgdesc = "Toolkit for Secure Sockets Layer and Transport Layer Security"
license = "Apache-2.0"
url = "https://www.openssl.org"
source = f"https://github.com/openssl/openssl/releases/download/openssl-{pkgver}/openssl-{pkgver}.tar.gz"
sha256 = "002a2d6b30b58bf4bea46c43bdd96365aaf8daa6c428782aa4feee06da197df3"
compression = "deflate"
# the codebase is not LTO-ready:
# https://github.com/openssl/openssl/issues/18663
# https://github.com/openssl/openssl/issues/22854
options = ["bootstrap", "!lto"]

if self.stage > 0:
    makedepends = ["linux-headers"]
else:
    configure_args += ["no-asm"]

#  if self.profile().cross:
#      configure_args += ["no-threads"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["enable-ec_nistp_64_gcc_128", "linux-x86_64"]
    case "aarch64" | "ppc64le" | "ppc64" | "ppc" | "x86":
        configure_args += [f"linux-{self.profile().arch}"]
    case "riscv64" | "loongarch64":
        configure_args += [f"linux64-{self.profile().arch}"]
    case "armhf" | "armv7":
        configure_args += ["linux-armv4"]
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"


def pre_configure(self):
    self.configure_args += self.get_cflags()
    self.configure_args += self.get_ldflags()


def build(self):
    self.make.invoke("depend")
    self.make.build(["MAKEDEPPROG=" + self.get_tool("CC")])


def post_install(self):
    # provided by ca-certificates
    self.uninstall("usr/bin/c_rehash")


def init_check(self):
    self.env["HARNESS_JOBS"] = str(self.make_jobs)


@subpackage("openssl3-libs")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libcrypto3"),
        self.with_pkgver("libssl3"),
    ]
    return self.default_libs(
        extra=["usr/lib/engines-3", "usr/lib/ossl-modules"]
    )


@subpackage("openssl3-devel")
def _(self):
    self.depends = [
        self.parent,
    ]
    self.provides = [self.with_pkgver("openssl-devel")]

    return self.default_devel()
