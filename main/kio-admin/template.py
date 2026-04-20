pkgname = "kio-admin"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DQT_MAJOR_VERSION=6", "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kio-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE KIO admin:// protocol implementation"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kio-admin"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-admin-{pkgver}.tar.xz"
sha256 = "843d321ca5bf902462f3906fb94768ab799aa354a31841761f71d090c5cbcdc0"
hardening = ["vis"]
