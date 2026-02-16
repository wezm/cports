pkgname = "modemmanager-qt"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["modemmanager-devel", "qt6-qttools-devel"]
checkdepends = ["dbus"]
depends = ["modemmanager"]
pkgdesc = "Qt ModemManager D-Bus API wrapper"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/modemmanager-qt/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/modemmanager-qt-{pkgver}.tar.xz"
sha256 = "2ac9b52efbce07ae055e25b7fb996c94e521218d83351c33f0060090ab98b63c"
hardening = ["vis"]


@subpackage("modemmanager-qt-devel")
def _(self):
    self.depends += ["modemmanager-devel"]

    return self.default_devel()
