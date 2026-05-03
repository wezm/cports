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
sha256 = "a7823ac8fcdd008faa29b1a63551eff2eaacf57c1f25445b0f84096adafae3ed"


def post_install(self):
    self.install_license("LICENSE")
