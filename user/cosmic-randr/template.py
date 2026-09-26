pkgname = "cosmic-randr"
pkgver = "1.9.0"
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
sha256 = "6c082cba6b80c5d89b02aec7ed315c9de8452cd413f5181ece43d7fdb3011481"


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-randr")
