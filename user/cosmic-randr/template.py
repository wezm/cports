pkgname = "cosmic-randr"
pkgver = "1.2.0"
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
sha256 = "1d8f75a4a3aa386ed44f5051eaa852b8742e745981e98ff4e903ed0384b1c617"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
