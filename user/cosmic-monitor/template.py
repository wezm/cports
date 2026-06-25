pkgname = "cosmic-monitor"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just"]
makedepends = [
    "rust-std",
]
pkgdesc = "COSMIC system monitor"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-monitor"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d56f46b679e79b19b87f753f683f29967e6c00f7b5a043e6bd5ca5c61658835d"
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
