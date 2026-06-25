pkgname = "cosmic-randr"
pkgver = "1.1.0"
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
sha256 = "5a95f60da4e89efb2c2ec8b35bd23bf35b2ef39e71e769cc73493f57ec2eb264"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
