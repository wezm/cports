pkgname = "kglobalaccel"
pkgver = "6.23.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Global desktop keyboard shortcuts"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kglobalaccel/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kglobalaccel-{pkgver}.tar.xz"
sha256 = "5760330e8aeb81542c44c94c26c109f74b7857c7c6b953d68d34e7079b6df70c"
hardening = ["vis"]


@subpackage("kglobalaccel-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
