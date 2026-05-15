pkgname = "libxml2-bootstrap"
pkgver = "2.15.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--with-history",
    "--with-icu",
    "--with-legacy",
    "--with-threads",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "icu-devel",
    "libedit-readline-devel",
    "ncurses-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
depends = ["!libxml2"]
pkgdesc = "Bootstrap version of libxml2"
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"$(GNOME_SITE)/libxml2/{pkgver[: pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "78262a6e7ac170d6528ebfe2efccdf220191a5af6a6cd61ea4a9a9a5042c7a07"


def post_install(self):
    self.install_license("Copyright")
