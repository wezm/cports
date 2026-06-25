pkgname = "cosmic-player"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libxkbcommon-devel",
    "rust-std",
]
depends = ["gst-plugins-good"]
pkgdesc = "COSMIC media player"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-player"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d3ccb0fcbd3ae82ba9efe1d9f0b9822d09f7a5f3abb94dd08199adf4a73d2881"
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
