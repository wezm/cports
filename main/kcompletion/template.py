pkgname = "kcompletion"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Powerful completion framework"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcompletion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcompletion-{pkgver}.tar.xz"
sha256 = "ad5c830bf5b63e5f7b792576aad726c827aad3ef6e2a0d35727be5feac44e176"
hardening = ["vis"]


@subpackage("kcompletion-devel")
def _(self):
    return self.default_devel()
