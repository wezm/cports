pkgname = "libzmf"
pkgver = "0.0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
make_dir = "."
hostmakedepends = [
    "automake",
    "doxygen",
    "librevenge-devel",
    "pkgconf",
    "slibtool",
]
makedepends = ["boost-devel", "icu-devel", "libpng-devel", "zlib-ng-devel"]
pkgdesc = "Import filter and tools for Zoner Callisto/Draw documents"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libzmf"
source = f"https://dev-www.libreoffice.org/src/libzmf/libzmf-{pkgver}.tar.xz"
sha256 = "27051a30cb057fdb5d5de65a1f165c7153dc76e27fe62251cbb86639eb2caf22"


@subpackage("libzmf-devel")
def _(self):
    return self.default_devel()
