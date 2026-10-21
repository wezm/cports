pkgname = "cosmic-monitor"
pkgver = "1.11.0"
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
sha256 = "c63aef9814982fd6dd1a0527c83bbe29c015154dee32a1ac9ce8f84290afd52b"
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
