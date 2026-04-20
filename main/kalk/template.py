pkgname = "kalk"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kunitconversion-devel",
    "libqalculate-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Calculator"
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://apps.kde.org/kalk"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kalk-{pkgver}.tar.xz"
sha256 = "e1e3159cf6f34a8df65c53e81f9f69ce3d2a316596fb45b766fe8e7484f3f09e"
hardening = ["vis"]
