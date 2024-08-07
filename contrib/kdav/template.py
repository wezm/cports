pkgname = "kdav"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE DAV library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdav/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdav-{pkgver}.tar.xz"
)
sha256 = "cf428935158984443fc0736252cf2e717065b76a72e6a42864c0dbe7581038ec"


@subpackage("kdav-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
