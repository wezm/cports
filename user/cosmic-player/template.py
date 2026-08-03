pkgname = "cosmic-player"
pkgver = "1.5.0"
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
sha256 = "0ec42af1124e4afcc2076a1c2e94cbda7f461dc84d3464f42169e2109515ea00"
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
