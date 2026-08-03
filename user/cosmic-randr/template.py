pkgname = "cosmic-randr"
pkgver = "1.5.0"
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
sha256 = "55b7d6070f05c12477f18c1c72beab9f1f5409cd83b63c31846c8c1739993aa2"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
