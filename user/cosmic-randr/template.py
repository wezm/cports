pkgname = "cosmic-randr"
pkgver = "1.10.0"
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
sha256 = "4556bc8954b212b74aabc60960c1f5f63af1c3cb3abe6b7e00d8278094a6ab1c"


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-randr")
