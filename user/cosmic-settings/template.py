pkgname = "cosmic-settings"
pkgver = "1.0.15"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "libinput-devel",
    "libxkbcommon-devel",
    "pipewire-devel",
    "rust-std",
    "udev-devel",
    "wayland-devel",
]
depends = [
    "accountsservice",
    "cosmic-icon-theme",
    "cosmic-randr",
    "iso-codes",
    "network-manager-applet",
    "xkeyboard-config",
]
pkgdesc = "Settings application for the COSMIC desktop"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-settings"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "4c158935aa652156dfa5ad8524666f4fb2ba2654ea9f6ec2d5fe94e0e6549e91"
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
