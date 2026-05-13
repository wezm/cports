pkgname = "cosmic-randr"
pkgver = "1.0.13"
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
sha256 = "f71f57173ddf8ecb1f9bbb70ae74555f7e7757f8fc0793a49bbb08b3f2bca3fc"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
