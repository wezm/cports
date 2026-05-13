pkgname = "cosmic-settings"
pkgver = "1.0.13"
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
sha256 = "62a8a8cb85ad7a75dbc9315d880c1367baf119040e80adff04a707f807811429"
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
