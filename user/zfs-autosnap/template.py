pkgname = "zfs-autosnap"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Automatic ZFS snapshot utility"
license = "MIT"
url = "https://github.com/wezm/zfs-autosnap"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a4acd45643ad816764612af0c38c9827454c0ebb6de90afdb321c3c3c23fd408"


def post_install(self):
    self.install_license("LICENSE")
