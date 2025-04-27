pkgname = "xcbproto"
pkgver = "1.17.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-legacy"]
hostmakedepends = ["pkgconf", "python", "automake"]
depends = ["python"]
pkgdesc = "XML-XCB (X C Bindings) protocol descriptions"
license = "MIT"
url = "https://xcb.freedesktop.org"
# source = f"https://gitlab.freedesktop.org/xorg/proto/xcbproto/-/archive/xcb-proto-{pkgver}/xcbproto-xcb-proto-{pkgver}.tar.gz"
source = f"https://xorg.freedesktop.org/archive/individual/proto/xcb-proto-{pkgver}.tar.gz"

sha256 = "392d3c9690f8c8202a68fdb89c16fd55159ab8d65000a6da213f4a1576e97a16"


def post_install(self):
    self.install_license("COPYING")
