pkgname = "cosmic-screenshot"
pkgver = "1.10.0"
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
sha256 = "1f74e8ac311e564dd1bac64a2bf02aa095e9c98222be832c2b3366124b3a5000"
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
