pkgname = "libxml2"
pkgver = "2.15.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-static",
    "--with-docs",
    "--with-history",
    "--with-icu",
    "--with-legacy",
    "--with-python",
    "--with-threads",
]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "doxygen",
    "libtool",
    "libxslt-progs",
    "pkgconf",
    "python-devel",
]
makedepends = [
    "icu-devel",
    "libedit-readline-devel",
    "ncurses-devel",
    "python-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "XML parsing library"
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"$(GNOME_SITE)/libxml2/{pkgver[: pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "78262a6e7ac170d6528ebfe2efccdf220191a5af6a6cd61ea4a9a9a5042c7a07"


def post_install(self):
    # Delete unwanted python static lib that gets built due to --enable-static
    self.uninstall("usr/lib/python*/site-packages/*.a", glob=True)
    self.install_license("Copyright")


@subpackage("libxml2-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends = ["python"]
    return ["usr/lib/python*"]


@subpackage("libxml2-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc/libxml2"])


@subpackage("libxml2-progs")
def _(self):
    return self.default_progs()
