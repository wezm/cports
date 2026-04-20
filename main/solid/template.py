pkgname = "solid"
pkgver = "6.25.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "ninja",
]
makedepends = [
    "libimobiledevice-devel",
    "libplist-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "udev-devel",
    "util-linux-mount-devel",
]
pkgdesc = "KDE Hardware integration and detection"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://develop.kde.org/docs/features/solid"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/solid-{pkgver}.tar.xz"
sha256 = "8177fa8f139b855856e171426c5f2adb96d727e62e6ec536675da11aa157b33e"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
