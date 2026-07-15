pkgname = "cosmic-launcher"
pkgver = "1.3.0"
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
sha256 = "d603f9c0fab552881cdd70673ed6134bc6d1e0086d413a703efcd9e926b7947e"
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
