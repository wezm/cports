pkgname = "prison"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "libdmtx-devel",
    "qrencode-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qttools-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE library to produce QR codes and DataMatrix barcodes"
license = "MIT"
url = "https://api.kde.org/frameworks/prison/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/prison-{pkgver}.tar.xz"
sha256 = "9d0c917649f39b685fd1b9298674680869ee013fbb82a2cfd6e733500b080236"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("prison-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
