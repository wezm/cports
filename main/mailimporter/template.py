pkgname = "mailimporter"
pkgver = "26.04.0"
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
    "akonadi-devel",
    "akonadi-mime-devel",
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kmime-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM library for importing mail"
license = "LGPL-2.0-or-later AND GPL-2.0-only"
url = "https://api.kde.org/kdepim/mailimporter/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/mailimporter-{pkgver}.tar.xz"
)
sha256 = "8e8034f9ebf2dec9b88662dd43c0ff367e250140e90803fa1e87072abe2333b1"


@subpackage("mailimporter-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
