pkgname = "kholidays"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE library for holiday dates"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kholidays/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kholidays-{pkgver}.tar.xz"
sha256 = "54c99aca6505c47eed1397ea259312a5b003ca5a622bfb4ecfe01ca6d7644e71"
hardening = ["vis"]


@subpackage("kholidays-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
