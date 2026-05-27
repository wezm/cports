pkgname = "cosmic-idle"
pkgver = "1.0.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "libxkbcommon-devel"]
pkgdesc = "COSMIC idle daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-idle"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "0d34d93e3941e006898a6f17bd6ab861db132fdcc1b1e841f688e149a78a2c16"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-idle")
