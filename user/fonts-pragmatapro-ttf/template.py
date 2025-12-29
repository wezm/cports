pkgname = "fonts-pragmatapro-ttf"
pkgver = "0.903"
pkgrel = 0
build_style = "meta"
pkgdesc = "Proprietary condensed monospace typeface"
license = "custom:meta"
url = "https://fsd.it/shop/fonts/pragmatapro"


def install(self):
    for f in (self.files_path).glob("*.ttf"):
        self.install_file(f, "usr/share/fonts/pragmatapro")
