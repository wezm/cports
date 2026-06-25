pkgname = "cosmic-term"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel", "wayland-devel", "zstd-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC terminal emulator"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-term"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "72ef099320fa6a33162b1adc8a0d85d91d47d76e0f1a0aa264dba60e07f63a37"


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
