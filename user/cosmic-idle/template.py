pkgname = "cosmic-idle"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "libxkbcommon-devel"]
pkgdesc = "COSMIC idle daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-idle"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "c305ca769949a8eb395fa40b26f28599e8961bd8df3cc3a97dc310209fccf39c"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-idle")
