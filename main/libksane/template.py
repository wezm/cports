pkgname = "libksane"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "gperf",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "ksanecore-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE image scanning library"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/graphics/libksane"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libksane-{pkgver}.tar.xz"
sha256 = "b2d4db16d41efc6dd502986e14a02277e02b94600ae042c26c6367a5cf301d77"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
