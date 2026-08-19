pkgname = "cosmic-panel"
pkgver = "1.6.0"
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
sha256 = "e0ada5834dfd8d1bf1aaff453c216f70bf632174893f05aef32bc656badbfab1"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-panel")

    default_schema = self.cwd / "data/default_schema"
    for p in default_schema.iterdir():
        if p.is_dir():
            self.install_files(p, "usr/share/cosmic")
