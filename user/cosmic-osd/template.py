pkgname = "cosmic-osd"
pkgver = "1.8.0"
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
sha256 = "bbd26d958173d9474cf4e6f89ffe1f3ff8aa57348748c3540001195e8f242cb2"
env = {"POLKIT_AGENT_HELPER_1": "/usr/lib/polkit-1/polkit-agent-helper-1"}
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
