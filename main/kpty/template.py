pkgname = "kpty"
pkgver = "6.25.0"
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
sha256 = "eb4deb424bdf20328dac0a12fdaab715dbf800e1cd08a4188cc2d3075543709f"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
