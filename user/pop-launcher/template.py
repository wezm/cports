pkgname = "pop-launcher"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "pop-launcher-bin"]
hostmakedepends = [
    "cargo-auditable",
    "just",
    "mesa-devel",
    "pkgconf",
]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
]
depends = [
    "dbus",
    "fd",
    "libqalculate-progs",
    "polkit",
    "pop-icon-theme",
    "xdg-utils",
]
pkgdesc = "Modular IPC-based desktop launcher service"
license = "MPL-2.0"
url = "https://github.com/pop-os/launcher"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "86907d81d7a97938076455be3b9e4f093fb90760a95c1e0558a04350e5701fb5"
# no tests
options = ["!check"]


def install(self):
    # TODO: the session scripts need to be reworked to not assume systemd
    _target_dir = f"target/{self.profile.triplet}/release"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"target-dir={_target_dir}",
        "install",
    )
    self.uninstall("usr/lib/pop-launcher/scripts/system76-power")
