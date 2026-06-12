pkgname = "cosmic-bg"
pkgver = "1.0.16"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC background image service"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-bg"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "b5dc91d77b3973d8c144c1b6cb975e6629b7ac11da21ca250c5cbb8a4f999de6"
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
