pkgname = "cosmic-wallpapers"
pkgver = "1.9.0"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d898a1a7f84c8138e9b16e6a0cc1ed806ce9a87a94ab75561895b8e1d7a465f5"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
