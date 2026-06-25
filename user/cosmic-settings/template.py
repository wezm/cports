pkgname = "cosmic-settings"
pkgver = "1.1.0"
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
sha256 = "c73dca78ef21bd402d703d46c363f81158a623120b6554fef2e4245944ede3ac"
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
