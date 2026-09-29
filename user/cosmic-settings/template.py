pkgname = "cosmic-settings"
pkgver = "1.9.0"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "dav1d-devel",
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
    "networkmanager",
    "xkeyboard-config",
]
pkgdesc = "Settings application for the COSMIC desktop"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-settings"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "1e33fec9dc70408a85eca4055dca16afa82baadc2edb957e1400294b09f2ff27"
# no tests
options = ["!check"]


def install(self):
    _target_dir = f"target/{self.profile.triplet}"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={_target_dir}",
        "install",
    )
