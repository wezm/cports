pkgname = "pop-launcher"
pkgver = "1.2.7"
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
    "libqalculate",
    "polkit",
    "pop-icon-theme",
    "xdg-utils",
]
pkgdesc = "Modular IPC-based desktop launcher service"
license = "MPL-2.0"
url = "https://github.com/pop-os/launcher"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e02ffd9876bb11c50118bf5e9c0bec57132f7010831da749dc6107e31ca198a6"
# no tests
options = ["!check"]


def install(self):
    # TODO: the session scripts need to be reworked to not assume systemd
    _target_dir = f"target/{self.profile().triplet}/release"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"target-dir={_target_dir}",
        "install",
    )
    self.uninstall("usr/lib/pop-launcher/scripts/system76-power")
