pkgname = "cosmic-randr"
pkgver = "1.11.0"
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
sha256 = "cd04841b780ad13d407a0a3740f827b3fc214dfc198b114d6a83524c2a0ca96e"


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-randr")
