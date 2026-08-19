pkgname = "cosmic-files"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "glib-devel", "libxkbcommon-devel", "zstd-devel"]
depends = ["cosmic-icon-theme", "gvfs", "xdg-utils"]
pkgdesc = "COSMIC file manager"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-files"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "c43251ffb09f443aaab1ce93c1a6a655fdc4f8a26c9615324bc85b6503fea210"
# examples/copy.rs fails to build
options = ["!check"]


def post_build(self):
    self.cargo.build(["--package", "cosmic-files-applet"])


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-files")
    self.install_bin(
        f"target/{self.profile().triplet}/release/cosmic-files-applet"
    )
    self.install_file(
        "target/xdgen/com.system76.CosmicFiles.metainfo.xml",
        "usr/share/metainfo",
    )
    self.install_file(
        "target/xdgen/com.system76.CosmicFiles.desktop",
        "usr/share/applications",
    )
    self.install_files("res/icons/hicolor", "usr/share/icons")
