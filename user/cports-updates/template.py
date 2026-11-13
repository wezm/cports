pkgname = "cports-updates"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["github-cli"]
pkgdesc = "Render cports-updates.txt"
license = "MIT"
url = "https://codeberg.org/wezm/cports-updates"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "aad2efe87c542902025d073c2c76a0bfb69a76d4a67082d8e9d72f525f71c2d1"


def post_install(self):
    self.install_license("LICENSE")
