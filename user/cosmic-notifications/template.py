pkgname = "cosmic-notifications"
pkgver = "1.0.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
    "wayland-devel",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC notification daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-notifications"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "ff43e58e79ea505bcf56bd301d92dc5539d65047b1a8f855a1fbe48093187da4"
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
