pkgname = "khealthcertificate"
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
    "kcodecs-devel",
    "ki18n-devel",
    "openssl3-devel",
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE library for health certificates"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/pim/khealthcertificate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/khealthcertificate-{pkgver}.tar.xz"
sha256 = "763026831a5c7c5f2e11e3656df940682c307a6b5746f683ebeea167a421565d"


@subpackage("khealthcertificate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
