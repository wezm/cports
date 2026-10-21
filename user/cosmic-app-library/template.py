pkgname = "cosmic-app-library"
pkgver = "1.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC application launcher"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-app-library"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "9ce3f012af1f885b0a99c589e77803c8d7fb76cba7a7202030cae19f1ac2dd55"
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
