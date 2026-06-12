pkgname = "cosmic-launcher"
pkgver = "1.0.16"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf", "intltool"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
]
depends = ["cosmic-icon-theme", "pop-launcher"]
pkgdesc = "COSMIC front-end for pop-launcher"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-launcher"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "82cc3b81f9da86e264b0f7e65320cc3e06e0ad654777de4eaba9b0c898333638"
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
