pkgname = "cosmic-monitor"
pkgver = "1.3.0"
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
sha256 = "891f8dff3dce8bbdc7c93fccd3b9b0fcc9276d6ead6206a508daa179d2468e1c"
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
