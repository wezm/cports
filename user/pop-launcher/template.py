pkgname = "pop-launcher"
pkgver = "1.6.0"
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
sha256 = "eb7d22712b03db50bf1a3629d133109275636b3d079501df8dfcb97fbe10d8fb"
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
