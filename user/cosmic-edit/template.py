pkgname = "cosmic-edit"
pkgver = "1.1.0"
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
sha256 = "8a254c3fc067f472f6b8f25880c8823b905b777647c136224f1da42e38464746"
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
