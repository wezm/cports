pkgname = "cosmic-initial-setup"
pkgver = "1.2.0"
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
sha256 = "20b2b4b3730f9cb26bc240416b97910c93212cc929d3101f35647654176cd06f"
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
