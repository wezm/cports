pkgname = "cosmic-wallpapers"
pkgver = "1.0.12"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a960dfdaa997f0052bd04c52d4694e463af28b28125ec6c783bc48373daeed3f"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
