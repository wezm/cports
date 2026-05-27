pkgname = "cosmic-term"
pkgver = "1.0.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel", "wayland-devel", "zstd-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC terminal emulator"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-term"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a87be2cd6af73be8ebcae4fe3f8b2777b89cbc3f5593df0623db749961f3e843"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-term")
    self.install_file(
        "target/xdgen/com.system76.CosmicTerm.metainfo.xml",
        "usr/share/metainfo",
    )
    self.install_file(
        "target/xdgen/com.system76.CosmicTerm.desktop",
        "usr/share/applications",
    )
    self.install_files("res/icons/hicolor", "usr/share/icons")
