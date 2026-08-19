pkgname = "zenith"
pkgver = "0.15.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "System resource monitor"
license = "MIT"
url = "https://github.com/bvaisvil/zenith"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "f92ed87b66f97b1f6c5863a62cc795ec877510dcd0284fba822ef5dc091b9355"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/zenith")
    self.install_license("LICENSE")
