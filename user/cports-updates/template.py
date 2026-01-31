pkgname = "cports-updates"
pkgver = "0.1.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["github-cli"]
pkgdesc = "Render cports-updates.txt"
license = "MIT"
url = "https://codeberg.org/wezm/cports-updates"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a8f1a2c187cb7a89f757f57fc0a2793cb7911e1c4f5b1a9eaeb30b5f7e4935c7"


def post_install(self):
    self.install_license("LICENSE")
