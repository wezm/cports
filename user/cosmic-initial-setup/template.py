pkgname = "cosmic-initial-setup"
pkgver = "1.3.0"
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
sha256 = "aeadf932dcf7d37681322af8822200edee3f91e5bef65b93f55492aa8ee9afc5"
# no tests
options = ["!check", "etcfiles"]


def install(self):
    _target_dir = f"target/{self.profile().triplet}"
    self.do(
        "just",
        f"rootdir={self.chroot_destdir}",
        f"cargo-target-dir={_target_dir}",
        "install",
    )
