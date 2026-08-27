pkgname = "cosmic-panel"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
    "wayland-devel",
]
pkgdesc = "COSMIC applet for creating panels and docks"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-panel"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "3bc2f7d6481a5ad221c9ee505fcc068a7c28df42c54e171cc6a4c86a5a64549e"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-panel")

    default_schema = self.cwd / "data/default_schema"
    for p in default_schema.iterdir():
        if p.is_dir():
            self.install_files(p, "usr/share/cosmic")
