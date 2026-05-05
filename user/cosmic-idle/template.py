pkgname = "cosmic-idle"
pkgver = "1.0.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "libxkbcommon-devel"]
pkgdesc = "COSMIC idle daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-idle"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d56498073c9f864fe2d3cf9bee588d65bae3afcaa3f0d2206751f95c74c8feff"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-idle")
