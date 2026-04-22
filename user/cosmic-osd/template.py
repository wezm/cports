pkgname = "cosmic-osd"
pkgver = "1.0.11"
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
depends = ["sound-theme-freedesktop"]
pkgdesc = "COSMIC on-screen display"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-osd"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "91442e62d97ed4e8d5db2ed05b7d0a7d60f6b9fb983fd46e640ef74d20db2614"
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
