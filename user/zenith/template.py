pkgname = "zenith"
pkgver = "0.14.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "System resource monitor"
license = "MIT"
url = "https://github.com/bvaisvil/zenith"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "b092048d1a9ce7234584d928e4b103aaaa7e47589923cf4e48dfa8919b3f8d88"
# no tests
options = ["!check"]


def post_extract(self):
    self.rm(".cargo/config")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/zenith")
    self.install_license("LICENSE")
