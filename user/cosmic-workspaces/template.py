pkgname = "cosmic-workspaces"
pkgver = "1.0.16"
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
sha256 = "aa974853ecd5e587f884f40c36c297412c6e4a2b46224284991edd9c49f5e7df"
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
