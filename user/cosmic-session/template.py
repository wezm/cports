pkgname = "cosmic-session"
pkgver = "1.0.16"
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
sha256 = "841eb967cb697269f7047ea7838c37a111ea85c6e6214d97ed3e8d275f45250c"
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
