pkgname = "qrca"
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
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kservice-devel",
    "networkmanager-qt-devel",
    "prison-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE QR code scanner"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/qrca"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/qrca-{pkgver}.tar.xz"
sha256 = "a08ccf498f9b2431e7572c57ccbb823f10d650274eafb5e5a83e9dc76d5ca1a9"
hardening = ["vis"]
