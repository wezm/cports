pkgname = "cosmic-workspaces"
pkgver = "1.0.15"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libinput-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "rust-std",
    "udev-devel",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC notification daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-workspaces-epoch"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a4a0d3ff668df7fbfa3909be20c23dd4e7fc1f5e89a6d67cd4f7bc575b805a92"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/cosmic-workspaces"
    )
    self.install_file(
        "data/com.system76.CosmicWorkspaces.desktop", "usr/share/applications"
    )
    self.install_file(
        "data/com.system76.CosmicWorkspaces.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
