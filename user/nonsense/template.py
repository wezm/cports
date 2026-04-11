pkgname = "nonsense"
pkgver = "0.1.2_git20250531"
pkgrel = 0
_gitrev = "9d34ed8"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
]
pkgdesc = "Nonsense web application"
license = "custom:none"
url = "https://forge.wezm.net/wezm/home.wezm.net"
source = f"https://forge.wezm.net/wezm/home.wezm.net/archive/{_gitrev}.tar.gz>nonsense-{pkgver}.tar.gz"
sha256 = "394c2961d90fb145d31942083ed90d27bcec00b107cca02521bf0959f930aaa4"


def post_install(self):
    self.install_service(self.files_path / "nonsense")
