pkgname = "cosmic-randr"
pkgver = "1.0.14"
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
sha256 = "6595b09c650816447f7d3332b2f62b0ed2d4d8b2ab06d88876853159a2daec3c"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
