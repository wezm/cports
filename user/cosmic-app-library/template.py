pkgname = "cosmic-app-library"
pkgver = "1.0.13"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC application launcher"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-app-library"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "b4f6637f6d4c6df412879c507d8264fda5c13a9ce3fbb4f607a42ec6c3eb892e"
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
