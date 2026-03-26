pkgname = "cosmic-edit"
pkgver = "1.0.8"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "glib-devel",
    "libxkbcommon-devel",
    "oniguruma-devel",
    "rust-std",
    "wayland-devel",
    "zstd-devel",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC text editor"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-edit"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d8dcd072b07523e27c114ff81787ed7cb0fb9a635900d1d368859c1759dfd5a3"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-edit")
    self.install_file(
        "target/xdgen/com.system76.CosmicEdit.metainfo.xml",
        "usr/share/metainfo",
    )
    self.install_file(
        "target/xdgen/com.system76.CosmicEdit.desktop",
        "usr/share/applications",
    )
    self.install_files("res/icons/hicolor", "usr/share/icons")
