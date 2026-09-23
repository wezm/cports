pkgname = "cosmic-viewer"
pkgver = "1.9.0"
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
sha256 = "a1c3b54c5f7dde278d17e4bd67395cd1ce4ef4a130ec1b0cfeebc05cc0ce3026"
env = {"TURBOJPEG_SOURCE": "pkg-config"}


def install(self):
    _target_dir = f"target/{self.profile.triplet}"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={_target_dir}",
        "install",
    )
