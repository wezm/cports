pkgname = "cosmic-launcher"
pkgver = "1.10.0"
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
sha256 = "6700ad7c036b323f877fbedd43d021f50128651af4265554466eb3847013774a"
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
