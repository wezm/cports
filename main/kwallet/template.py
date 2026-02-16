pkgname = "kwallet"
pkgver = "6.23.0"
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
    "gpgme-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libgcrypt-devel",
    "libsecret-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Safe desktop-wide storage for passwords"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kwallet/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kwallet-{pkgver}.tar.xz"
sha256 = "0cf8bd17c3300c71245c25d4e0fee513b7305ccd97f28d9a4c8e325283337a27"
hardening = ["vis"]


@subpackage("kwallet-devel")
def _(self):
    return self.default_devel()
