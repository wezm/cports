pkgname = "cports-updates"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["github-cli"]
pkgdesc = "Render cports-updates.txt"
license = "MIT"
url = "https://codeberg.org/wezm/cports-updates"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c80dc03808e1c1f7f095f2ebd6d7edb877a94d7dd579547a8e4ec5ae0d190a72"


def post_install(self):
    self.install_license("LICENSE")
