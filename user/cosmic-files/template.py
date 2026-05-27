pkgname = "cosmic-files"
pkgver = "1.0.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "glib-devel", "libxkbcommon-devel", "zstd-devel"]
depends = ["cosmic-icon-theme", "gvfs", "xdg-utils"]
pkgdesc = "COSMIC file manager"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-files"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a8afeffe9b4e47916a79e6344724446870dd0f10cce97dfdd7964705402f416c"
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
