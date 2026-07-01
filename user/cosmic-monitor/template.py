pkgname = "cosmic-monitor"
pkgver = "1.2.0"
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
sha256 = "8dca207ef71a91652412da5273b431b8ffd6c092e3860d7dd09e4056e407a03f"
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
