pkgname = "hexyl"
pkgver = "0.17.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Command-line hex viewer with colored output"
license = "Apache-2.0 OR MIT"
url = "https://github.com/sharkdp/hexyl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "72fa17397ad187eec6b295d02c7caabbb209a6e0d5706187b8a599bd5df8615e"


def post_install(self):
    self.install_license("LICENSE-MIT")
