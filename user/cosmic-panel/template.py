pkgname = "cosmic-panel"
pkgver = "1.0.11"
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
sha256 = "7e5e96686d4fd5445ccaee5d7cc4134a2adc9f829098b9cf5dbcaa32718ae82f"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-panel")

    default_schema = self.cwd / "data/default_schema"
    for p in default_schema.iterdir():
        if p.is_dir():
            self.install_files(p, "usr/share/cosmic")
