pkgname = "kdoctools"
pkgver = "6.25.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "docbook-xsl",
    "extra-cmake-modules",
    "gettext",
    "libxml2-progs",
    "ninja",
    "perl",
    "perl-uri",
]
makedepends = [
    "karchive-devel",
    "ki18n-devel",
    "libxslt-devel",
    "qt6-qttools-devel",
]
depends = ["docbook-xsl", "libxml2-progs"]
provides = [self.with_pkgver("kdoctools-doc")]
pkgdesc = "KDE Documentation generation from docbook"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kdoctools/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdoctools-{pkgver}.tar.xz"
sha256 = "2c5866257edda20f33c35f64a8bcab08de3dddb4e751bbbc2e09e941df979918"
hardening = ["vis"]
# the "docs" are really common stylesheets that are needed
# by things using kdoctools so make sure they get installed
options = ["!splitdoc"]


@subpackage("kdoctools-devel")
def _(self):
    return self.default_devel()
