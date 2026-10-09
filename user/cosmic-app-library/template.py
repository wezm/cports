pkgname = "cosmic-app-library"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC application launcher"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-app-library"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "43ce4f50c97d2106ac981080d8372e03c50af28660a6737400920ecbc6ce4b39"
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
