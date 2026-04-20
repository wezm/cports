pkgname = "yakuake"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "kwayland-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = ["konsole"]
pkgdesc = "KDE drop-down terminal"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/yakuake"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/yakuake-{pkgver}.tar.xz"
sha256 = "98c56fd23155e528f5136583de7700109cc4812dd5bc6c7d8940046f020223c5"
