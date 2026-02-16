pkgname = "kpty"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = ["kcoreaddons-devel", "ki18n-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Interface to pseudo terminal devices"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpty/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "a1218eb6b9cc52f26d1e47923f8458d7c6712dced759860371ad330285a5b951"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
