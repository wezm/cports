pkgname = "cosmic-randr"
pkgver = "1.3.0"
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
sha256 = "df4a0827325f45323f3646048e3528b6b7a05f12d3fc77353fa88cfb86118fdd"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
