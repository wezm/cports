pkgname = "kdenetwork-filesharing"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
]
# net, testparm
depends = ["samba-common"]
pkgdesc = "KDE samba filesharing plugin"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenetwork_filesharing"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenetwork-filesharing-{pkgver}.tar.xz"
sha256 = "c53fe19f37153d14fdf84181c4edffe368d4dc2196cce510c88ad8ebe71f9b01"
