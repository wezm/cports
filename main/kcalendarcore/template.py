pkgname = "kcalendarcore"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = ["libical-devel", "qt6-qtdeclarative-devel", "qt6-qttools-devel"]
checkdepends = ["perl", "xwayland-run"]
pkgdesc = "KDE calendar access library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kcalendarcore/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcalendarcore-{pkgver}.tar.xz"
sha256 = "4e0c610cab31de9375d1f3cd86f8d225f9f710d7e2e7121920ef3da369c4064b"
# a ton of failures due to different sort order and whatnot
options = ["!check"]


@subpackage("kcalendarcore-devel")
def _(self):
    return self.default_devel()
