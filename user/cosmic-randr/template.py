pkgname = "cosmic-randr"
pkgver = "1.0.16"
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
sha256 = "1b748ffd2e4dccf01ad947dfdd63d09d420ec7a922000aac3c39418dee9fb5f5"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
