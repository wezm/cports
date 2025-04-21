pkgname = "nonsense"
pkgver = "0.1.2_git20250420"
pkgrel = 0
_gitrev = "27dc77c"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
]
pkgdesc = "Nonsense web application"
license = "custom:none"
url = "https://forge.wezm.net/wezm/home.wezm.net"
source = f"https://forge.wezm.net/wezm/home.wezm.net/archive/{_gitrev}.tar.gz>nonsense-{pkgver}.tar.gz"
sha256 = "7bdbadb1e1f4b1fceadb7a8f3ccce3ec0b0a5b2d3b9e776e2d9dc13682d906c4"


def post_install(self):
    self.install_service(self.files_path / "nonsense")
