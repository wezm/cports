pkgname = "cosmic-randr"
pkgver = "1.0.11"
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
sha256 = "fcef1f631c664c028d9b4f6b18a58993a42b31183bfe1d44823261668e7fcdc1"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
