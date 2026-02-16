pkgname = "kcmutils"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Utilities for KDE System Settings modules"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcmutils/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcmutils-{pkgver}.tar.xz"
sha256 = "54ecfedc0bc91ce95fa98b8b53e41d2993557e99a19b953395c2a5e5dc4210f8"
hardening = ["vis"]


@subpackage("kcmutils-devel")
def _(self):
    self.depends += [
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "qt6-qtdeclarative-devel",
    ]

    return self.default_devel()
