pkgname = "cosmic-screenshot"
pkgver = "1.0.11"
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
sha256 = "83284dbe7bb6b729c291dc661c41b59802504329295d8a89aeee36ad5d28df5a"
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
