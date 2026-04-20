pkgname = "kitemviews"
pkgver = "6.25.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Widget addons for Qt Model/View"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://api.kde.org/frameworks/kitemviews/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kitemviews-{pkgver}.tar.xz"
sha256 = "b57f38d6fd184a4b260d0b35d76f6c0fb96bdd80475e3ca7d4151023730e5d3d"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kitemviews-devel")
def _(self):
    return self.default_devel()
