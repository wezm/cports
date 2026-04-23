pkgname = "cosmic-randr"
pkgver = "1.0.8"
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
sha256 = "ea8f96ce37566e85b61f0397d06940702db01d83cffbf9ca33ff6e3a38cbff2e"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
