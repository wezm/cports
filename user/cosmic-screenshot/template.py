pkgname = "cosmic-screenshot"
pkgver = "1.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "rust-std",
]
depends = ["cosmic-icon-theme", "xdg-desktop-portal-cosmic"]
pkgdesc = "COSMIC screenshot utility"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-screenshot"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "0bf658bda69ce67113d58d1ad5d32126218095194cc51f69c27b8d6399962af7"
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
