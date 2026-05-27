pkgname = "cosmic-initial-setup"
pkgver = "1.0.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "libinput-devel",
    "libpulse-devel",
    "libxkbcommon-devel",
    "rust-std",
    "zstd-devel",
]
depends = ["cosmic-icon-theme", "polkit"]
pkgdesc = "COSMIC background image service"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-initial-setup"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "f747fce8126b0334da4b4f0842b00b6262b2f3df25ced3530ba086d814bc7388"
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
