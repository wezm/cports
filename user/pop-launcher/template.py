pkgname = "pop-launcher"
pkgver = "1.0.14"
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
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "6b4f7f27d0cf44d24e1e24141210dfb87badff2e06cfa47a05e411ebd4d86de3"
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
