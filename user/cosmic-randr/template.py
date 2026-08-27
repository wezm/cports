pkgname = "cosmic-randr"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "rust-std",
    "wayland-devel",
]
pkgdesc = "Utility for displaying and configuring Wayland outputs"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-randr"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "226591921a26f0fa03cf3867b73d7d1af89bda16f4ea45eea75decd0bbcd1e29"


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-randr")
