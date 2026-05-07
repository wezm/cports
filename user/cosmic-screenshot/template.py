pkgname = "cosmic-screenshot"
pkgver = "1.0.12"
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
sha256 = "b94d517c34cddb218373ffca80a365b6dde84a28e6d4bf3d7e56df841db45625"
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
