pkgname = "iperf"
pkgver = "3.20"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "slibtool",
]
makedepends = ["openssl3-devel"]
pkgdesc = "IP bandwidth measurement tool"
license = "BSD-3-Clause-LBNL"
url = "https://github.com/esnet/iperf"
# source = f"{url}/releases/download/{pkgver}/iperf-{pkgver}.tar.gz"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "84640ea0f43831850434e50134d0554b7a94f97fb02e2488ffbe252c9fb05a56"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iperf-devel")
def _(self):
    return self.default_devel()
