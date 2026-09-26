pkgname = "cosmic-player"
pkgver = "1.9.0"
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
sha256 = "d2a13306348cdc3886f75c918f00e3722ec85509d0b7f286023f3929b7aa0600"
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
