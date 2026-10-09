pkgname = "cosmic-idle"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "libxkbcommon-devel"]
pkgdesc = "COSMIC idle daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-idle"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "532074f48a9c0c23bebfcc171b527a732fa8850ce83f3cd2f4ca5926ef6fbac7"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-idle")
