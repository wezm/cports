pkgname = "pngcrush"
pkgver = "1.8.13"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["libpng-devel", "zlib-ng-devel"]
pkgdesc = "Tool for optimizing the compression of PNG files"
license = "custom:pngcrush"
url = "http://pmt.sourceforge.net/pngcrush"
source = f"https://downloads.sourceforge.net/pmt/pngcrush-{pkgver}-nolib.tar.xz"
sha256 = "3b4eac8c5c69fe0894ad63534acedf6375b420f7038f7fc003346dd352618350"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
