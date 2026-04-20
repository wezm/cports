pkgname = "kio-zeroconf"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kdbusaddons-devel",
    "kdnssd-devel",
    "ki18n-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE KIO zeroconf support"
license = "GPL-2.0-or-later AND LGPL-2.0-only"
url = "https://invent.kde.org/network/kio-zeroconf"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kio-zeroconf-{pkgver}.tar.xz"
)
sha256 = "db2e089f15883e33f4cfa971cfe232b0ee2f4f0505b0a276f867d3a44fe84ae1"
hardening = ["vis"]
