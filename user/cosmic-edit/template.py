pkgname = "cosmic-edit"
pkgver = "1.6.0"
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
sha256 = "bc64ead5c0893db7cd67594ef5d9ba2a85b1dee23aed5c625428d8ec1d13381f"
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
