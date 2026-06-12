pkgname = "cosmic-term"
pkgver = "1.0.16"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel", "wayland-devel", "zstd-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC terminal emulator"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-term"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d595d1e30d1f7338399950f3dd2aadcb59d04c34e25b355258caf5f7cb8d8a29"


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
