pkgname = "zfs-autosnap"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Automatic ZFS snapshot utility"
license = "MIT"
url = "https://codeberg.org/wezm/zfs-autosnap"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "751a0ad2fed3c50a4b1e29fe1f44bfe47838511bb0ce166505297a902a48f9d9"


def post_install(self):
    self.install_license("LICENSE")
