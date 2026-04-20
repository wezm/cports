pkgname = "kweathercore"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
# needs to get location
make_check_args = ["-E", "locationquerytest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kholidays-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
    "qt6-qtpositioning-devel",
]
pkgdesc = "KDE Weather library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kweathercore/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kweathercore-{pkgver}.tar.xz"
)
sha256 = "5d2f47c6b47a352911c1697704bc0a6fd51fe93807def98aab4bdc193e7dcc3b"


@subpackage("kweathercore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
