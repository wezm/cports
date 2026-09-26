pkgname = "cosmic-monitor"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
]
pkgdesc = "COSMIC system monitor"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-monitor"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "2ef7102ddfc982bd4c3e70632bce1b0e5bb2d6d96fb830a3ac8db0b2fff47709"
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
