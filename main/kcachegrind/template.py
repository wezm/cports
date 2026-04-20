pkgname = "kcachegrind"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE profiling visualisation tool"
license = "GPL-2.0-only"
url = "https://apps.kde.org/kcachegrind"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcachegrind-{pkgver}.tar.xz"
sha256 = "476919c3a9bec436b1a55a6c1a28ebfb07b43d6e22c05c6a476d0bfa537c8fa4"
hardening = ["vis"]


def post_install(self):
    # python2
    self.uninstall("usr/bin/hotshot2calltree")


@subpackage("kcachegrind-scripts")
def _(self):
    self.subdesc = "perl script utilities"
    self.install_if = [self.parent]
    self.depends += ["perl"]

    return [
        "usr/bin/dprof2calltree",
        "usr/bin/memprof2calltree",
        "usr/bin/op2calltree",
        # technically the above is a lie and this is php, but it also needs a pear plugin for Console_Getopt, so whatever
        "usr/bin/pprof2calltree",
    ]
