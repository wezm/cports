pkgname = "cosmic-viewer"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "dav1d-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libxkbcommon-devel",
    "rust-std",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC image viewer"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-viewer"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "ac0cee420c954b85188d1fbfffee32a49d11dacced881c68b068c56e83efcdad"
env = {"TURBOJPEG_SOURCE": "pkg-config"}


def install(self):
    _target_dir = f"target/{self.profile.triplet}"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={_target_dir}",
        "install",
    )
