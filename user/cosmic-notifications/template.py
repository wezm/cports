pkgname = "cosmic-notifications"
pkgver = "1.0.12"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = [
    "libxkbcommon-devel",
    "rust-std",
    "wayland-devel",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC notification daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-notifications"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "ea2bef34f445ba11eaf5eaf674ea9fc0697c5fc3a1568312a0eedfe9a129de4d"
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
