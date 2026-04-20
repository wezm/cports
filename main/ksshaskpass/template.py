pkgname = "ksshaskpass"
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
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE askpass helper"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/ksshaskpass"
source = f"$(KDE_SITE)/plasma/{pkgver}/ksshaskpass-{pkgver}.tar.xz"
sha256 = "46f3606c1591986091d9b289c491512e8c058216a71f20ccdcad32d5b02a4393"
