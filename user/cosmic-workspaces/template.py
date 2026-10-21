pkgname = "cosmic-workspaces"
pkgver = "1.11.0"
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
sha256 = "4dad3cd1fffe5b377c84948598c666493e5a053e6e1105a958f20a73bea92eab"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-workspaces")
    self.install_file(
        "data/com.system76.CosmicWorkspaces.desktop", "usr/share/applications"
    )
    self.install_file(
        "data/com.system76.CosmicWorkspaces.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
