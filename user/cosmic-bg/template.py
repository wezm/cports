pkgname = "cosmic-bg"
pkgver = "1.0.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "just", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC background image service"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-bg"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a47777270928fa871e1001bd6ab5bb5065aae722d88eaf7c7ee7cbd8af47234c"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-bg")
    self.do(
        "just",
        "appid=com.system76.CosmicBackground",
        f"install-dir={self.chroot_destdir}/usr/share",
        "install",
        wrksrc=self.chroot_srcdir / "data",
    )
    self.do(
        "just",
        "appid=com.system76.CosmicBackground",
        f"install-dir={self.chroot_destdir}/usr/share",
        "install",
        wrksrc=self.chroot_srcdir / "data/icons",
    )
