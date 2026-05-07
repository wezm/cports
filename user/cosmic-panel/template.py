pkgname = "cosmic-panel"
pkgver = "1.0.12"
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
sha256 = "665344cfb1bab8972d872d0ff06e66090084d68b8136d239374607448afdce92"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-panel")

    default_schema = self.cwd / "data/default_schema"
    for p in default_schema.iterdir():
        if p.is_dir():
            self.install_files(p, "usr/share/cosmic")
