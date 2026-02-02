pkgname = "cports-updates"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["github-cli"]
pkgdesc = "Render cports-updates.txt"
license = "MIT"
url = "https://codeberg.org/wezm/cports-updates"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "98348e3d3d637618b028d2690be6ad83f8d93ade1908de881136d33d4dd80700"


def post_install(self):
    self.install_license("LICENSE")
