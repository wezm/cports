pkgname = "cosmic-initial-setup"
pkgver = "1.0.11"
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
sha256 = "b224de79238272cb66014326b86d8b579aac53d844d86b24be76caba23b9a2e2"
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
