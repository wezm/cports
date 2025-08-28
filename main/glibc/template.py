_trip = "x86_64-pc-linux-gnu"
pkgname = f"glibc"
pkgver = "2.42"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    # TODO: cross
    #  f"--host={_trip}"
    #  "--build=$(../scripts/config.guess)"
    # "--with-headers=/usr/include",
    #  "--with-bugurl=https://bugs.archlinux.org/",
    #  "--sbindir=/usr/bin",
    #  "--libdir=/usr/lib",
    #  "--mandir=/usr/share/man",
    #  "--infodir=/usr/share/info",
    "--enable-bind-now",
    "--enable-cet",
    "--enable-fortify-source",
    "--enable-kernel=4.4",  # LFS uses 4.14, drawbacks to that?
    #  "--enable-multi-arch",
    "--enable-stack-protector=strong",
    "--disable-profile",
    "--disable-werror",
    "--with-gd=no",
]
make_cmd = "gmake"
# These auxiliary programs are missing or incompatible versions: msgfmt makeinfo
# FIXME: binutils
hostmakedepends = [
    "binutils-x86_64",
    "gmake",
    "gawk",
    "bison",
    "python",
    "gcc",
]  # FIXME: needs makeinfo if docs
makedepends = ["linux-headers"]
pkgdesc = "GNU libc"
# maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libc"
source = f"$(GNU_SITE)/glibc/glibc-{pkgver}.tar.xz"
# [azanella/clang] 6bc4b13
# source = "https://files.wezm.net/chimera/glibc.tar.xz"
sha256 = "d1775e32e4628e64ef930f435b67bb63af7599acb6be2b335b9f19f16509f17f"
tools = {
    "CC": "gcc",
    "CXX": "g++",
    "AS": "as",
    "LD": "ld.bfd",
    "OBJDUMP": "gobjdump",
}
# resistance is futile
options = ["bootstrap", "!check", "!lto"]  # TODO: check

configure_gen = []

#  if self.stage > 0:
#      configure_args += ["--enable-systemtap"]


def pre_configure(self):
    build_dir = self.cwd / self.make_dir
    build_dir.mkdir()
    with open(build_dir / "configparms", "w") as cf:
        cf.write(
            """
slibdir=/usr/lib
libdir=/usr/lib
rtlddir=/usr/lib
sbindir=/usr/bin
rootsbindir=/usr/bin
"""
        )


#  def post_configure(self):
#      1 / 0


def post_install(self):
    # fix up hardlinks
    self.rm(self.destdir / "usr/libexec/getconf/POSIX_V7_LP64_OFF64")
    self.install_link(
        "POSIX_V6_LP64_OFF64", "usr/libexec/getconf/POSIX_V7_LP64_OFF64"
    )

    self.rm(self.destdir / "usr/libexec/getconf/XBS5_LP64_OFF64")
    self.install_link(
        "POSIX_V6_LP64_OFF64", "usr/libexec/getconf/XBS5_LP64_OFF64"
    )

    self.rm(self.destdir / "usr/bin/getconf")
    self.install_link(
        "../libexec/getconf/POSIX_V6_LP64_OFF64", "usr/bin/getconf"
    )

    #  self.install_link("lib", "usr/lib64")


@subpackage("glibc-devel")
def _(self):
    return self.default_devel()
