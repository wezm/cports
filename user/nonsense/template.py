pkgname = "nonsense"
pkgver = "0.1.2_git20250421"
pkgrel = 0
_gitrev = "ce975fa"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
]
pkgdesc = "Nonsense web application"
license = "custom:none"
url = "https://forge.wezm.net/wezm/home.wezm.net"
source = f"https://forge.wezm.net/wezm/home.wezm.net/archive/{_gitrev}.tar.gz>nonsense-{pkgver}.tar.gz"
sha256 = "fb0d00de554d50bf2e07ed9e8466c68158f55724c016b39fed94c872b95d6315"


def post_install(self):
    self.install_service(self.files_path / "nonsense")
