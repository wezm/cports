_trip = "x86_64-pc-linux-gnu"
pkgname = f"binutils"
pkgver = "2.41"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--target={_trip}",
    f"--with-sysroot=/usr/{_trip}",
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--without-debuginfod",
    "--with-system-zlib",
    "--with-zstd=no", # TODO: only do this when bootstrap?
    "--with-msgpack=no",
    #  "--with-mmap",
    #  "--with-pic",
    #  "--disable-install-libbfd",
    "--disable-multilib",
    "--disable-werror",
    "--disable-shared",
    "--disable-gold",
    #  "--disable-nls",
    "--enable-gprofng=no",
    #  "--enable-default-hash-style=gnu",
    #  "--enable-deterministic-archives",
    #  "--enable-64-bit-bfd",
    #  "--enable-threads",
    #  "--enable-plugins",
    #  "--enable-relro",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "flex", "texinfo"]
makedepends = ["zlib-devel"] #, "libfl-devel-static"]
pkgdesc = "GNU binutils"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/binutils"
source = f"$(GNU_SITE)/binutils/binutils-{pkgver}.tar.xz"
sha256 = "ae9a5789e23459e59606e6714723f2d3ffc31c03174191ef0d015bdf06007450"
# resistance is futile
options = ["bootstrap", "!check", "!lto"]

if self.stage == 0:
    options += ["!scanrundeps"]

if self.profile().cross:
    configure_args += [
        f"--host={self.profile().triplet}",
        f"--with-build-sysroot={self.profile().sysroot}",
    ]


def post_install(self):
    # fix up hardlinks
    for f in (self.destdir / f"usr/{_trip}/bin").iterdir():
        self.rm(self.destdir / f"usr/bin/{f.name}")
        self.install_link(
            f"../{_trip}/bin/{f.name}", f"usr/bin/{f.name}"
        )
    # this is also a hardlink
    self.rm(self.destdir / f"usr/{_trip}/bin/ld")
    self.install_link("ld.bfd", f"usr/{_trip}/bin/ld")
    # remove unnecessary dupe
    self.rm(self.destdir / "usr/lib", recursive=True)


configure_gen = []
