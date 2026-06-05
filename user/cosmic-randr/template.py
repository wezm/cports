pkgname = "cosmic-randr"
pkgver = "1.0.15"
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
sha256 = "c6892430ab2efe1b778bfa353a7d51f6766c07b1103dbe14021a1f540e57900a"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
