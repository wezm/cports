pkgname = "cosmic-randr"
pkgver = "1.0.12"
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
sha256 = "e25c4a165ea48da10b3a31afaa49ff66f020971c1428a9785a807fb27b9bb52d"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
