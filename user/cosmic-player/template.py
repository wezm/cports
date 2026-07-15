pkgname = "cosmic-player"
pkgver = "1.3.0"
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
sha256 = "f3045901d23c579458374b484bacc9bb7f083f4940c40d94d3523dc809e57d3e"
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
