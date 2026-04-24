pkgname = "cosmic-applets"
pkgver = "1.0.8"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "pipewire-devel",
    "rust-std",
    "udev-devel",
    "wayland-devel",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "Applets for COSMIC panel"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-applets"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "75738474a60447922412e771d7cdf691218143c3acc22c8ebd0174ba78354790"
# no tests
options = ["!check"]


def install(self):
    _target_dir = f"target/{self.profile().triplet}"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"targetdir={_target_dir}",
        "install",
    )
    # TODO: dinit service
    # bldroot/destdir/cosmic-applets-1.0.8/cosmic-applets/usr/lib/systemd/user/com.system76.CosmicStatusNotifierWatcher.service
    self.uninstall("usr/lib/systemd")
