pkgname = "cosmic-idle"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "libxkbcommon-devel"]
pkgdesc = "COSMIC idle daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-idle"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "b35c98a998687aca66cedbb02d5067c8de4a8340f8c3e12a4b7c44adfa59ef52"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-idle")
