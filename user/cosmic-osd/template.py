pkgname = "cosmic-osd"
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
depends = ["sound-theme-freedesktop"]
pkgdesc = "COSMIC on-screen display"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-osd"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "0328dca2306639ebfa3e9b8610d1068fe5ea003dcf5b248c61d6443a10a8bd39"
env = {"POLKIT_AGENT_HELPER_1": "/usr/lib/polkit-1/polkit-agent-helper-1"}
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
