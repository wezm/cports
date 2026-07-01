pkgname = "cosmic-launcher"
pkgver = "1.2.0"
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
sha256 = "c3168ca353f89292499c0a8aa8f0a572f4ddbe749fa1830202f8d47dee741122"
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
