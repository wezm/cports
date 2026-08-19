pkgname = "cosmic-randr"
pkgver = "1.6.0"
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
sha256 = "664f09f9e872b8cc0a9223bb6d15188eb854f61d9b722dfa82977d6aab88cd14"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-randr")
