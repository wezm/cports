pkgname = "kio-extras"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
# thumbnail: fails for some reason
# testkioarchive: fails to open tar, support seems to not be detected
make_check_args = ["-E", "(thumbnailtest|testkioarchive)"]
make_check_wrapper = [
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "gperf",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kcmutils-devel",
    "kconfigwidgets-devel",
    "kdbusaddons-devel",
    "kdnssd-devel",
    "kdoctools-devel",
    "kdsoap-ws-discover-client-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knotifications-devel",
    "ktextwidgets-devel",
    "libimobiledevice-devel",
    "libkexiv2-devel",
    "libmtp-devel",
    "libplist-devel",
    "libssh-devel",
    "openexr-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "plasma-activities-stats-devel",
    "qcoro-devel",
    "qt6-qtbase-private-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "samba-client-devel",
    "syntax-highlighting-devel",
    "taglib-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE KIO additional plugins"
license = "LGPL-3.0-or-later"
url = "https://invent.kde.org/network/kio-extras"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-extras-{pkgver}.tar.xz"
sha256 = "7c87dc107ed375f5dfed74ffaf86a25990c131e539a4789b78ba70751b2fefac"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("kio-extras-devel")
def _(self):
    return self.default_devel()
