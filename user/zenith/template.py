pkgname = "zenith"
pkgver = "0.15.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["linux-headers", "rust-std"]
pkgdesc = "System resource monitor"
license = "MIT"
url = "https://github.com/bvaisvil/zenith"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "ffa3412c19e99f9ef691f86e4f9b1a342add2b0504bb3ea7f0b57daa17e4b731"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/zenith")
    self.install_license("LICENSE")
