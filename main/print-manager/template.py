pkgname = "print-manager"
pkgver = "6.6.4"
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
    "kcmutils-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["cups"]
pkgdesc = "KDE tool for printers"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/print-manager"
source = f"$(KDE_SITE)/plasma/{pkgver}/print-manager-{pkgver}.tar.xz"
sha256 = "ec44822dd2b2ecf5f26c36f9a46d5cbb3ee01d0b75ca0a2ad95f98a53d93ce6e"
hardening = ["vis"]
