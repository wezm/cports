pkgname = "libopusenc"
pkgver = "0.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["opus-devel"]
pkgdesc = "Library for encoding Opus files"
license = "BSD-3-Clause"
url = "https://opus-codec.org"
source = f"https://downloads.xiph.org/releases/opus/libopusenc-{pkgver}.tar.gz"
sha256 = "f616d3aff9b2034547894ccb8ab56c36cf1a4acb0d922c5d7119f97bbe58642c"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libopusenc-devel")
def _(self):
    return self.default_devel()
