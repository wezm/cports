pkgname = "cosmic-app-library"
pkgver = "1.0.16"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC application launcher"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-app-library"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "f854824cf91a1d20b8d85b6d3297226548c7c630b2f498bc309df320b25bfa5d"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/cosmic-app-library"
    )
    self.do(
        "just",
        "appid=com.system76.CosmicAppLibrary",
        f"install-dir={self.chroot_destdir}/usr/share",
        "install",
        wrksrc=self.chroot_srcdir / "data",
    )
    self.do(
        "just",
        "appid=com.system76.CosmicAppLibrary",
        f"install-dir={self.chroot_destdir}/usr/share",
        "install",
        wrksrc=self.chroot_srcdir / "data/icons",
    )
