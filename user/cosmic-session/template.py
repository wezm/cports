pkgname = "cosmic-session"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
    "wayland-devel",
]
depends = [
    "cosmic-app-library",
    "cosmic-applets",
    "cosmic-bg",
    "cosmic-comp",
    "cosmic-files",
    "cosmic-greeter",
    "cosmic-icon-theme",
    "cosmic-idle",
    "cosmic-launcher",
    "cosmic-notifications",
    "cosmic-osd",
    "cosmic-panel",
    "cosmic-randr",
    "cosmic-screenshot",
    "cosmic-settings",
    "cosmic-settings-daemon",
    "cosmic-workspaces",
    "fonts-opensans-ttf",
    "xdg-desktop-portal-cosmic",
    "xwayland",
    #  "noto-fonts",
    #  "switcheroo-control",
    #  "vulkan-driver",
]
pkgdesc = "Session manager for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-session"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "f2b1bc36cbc0a4dff2e2647c7bbaf1e53ed4fc6a13360110a5ffa8fc2922ce1d"
# no tests
options = ["!check"]


def install(self):
    _target_dir = f"target/{self.profile().triplet}"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={_target_dir}",
        "install",
    )
    # TODO: dinit service for cosmic-session.target
    self.uninstall("usr/lib/systemd")
