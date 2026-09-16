pkgname = "samply"
pkgver = "0.13.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "sqlite-devel"]
pkgdesc = "Sampling profiler"
license = "MIT OR Apache-2.0"
url = "https://github.com/mstange/samply"
source = f"{url}/archive/samply-v{pkgver}.tar.gz"
sha256 = "7002789471f8ef3a36f4d4db7be98f2847724e2b81a53c5e23d5cae022fb704b"


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/samply")
    self.install_license("LICENSE-MIT")
