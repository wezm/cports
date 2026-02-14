pkgname = "qt6-qtsvg"
pkgver = "6.10.2"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = ["-E", "module_includes"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "qt6-qtbase"]
makedepends = ["qt6-qtbase-private-devel"]
pkgdesc = "Qt6 SVG component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtsvg-everywhere-src-{pkgver}.tar.xz"
sha256 = "f07ff80f38caf235187200345392ca7479445ddf49a36c3694cd52a735dad6e1"
# FIXME
hardening = ["!int"]


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtsvg-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
