pkgname = "cosmic-wallpapers"
pkgver = "1.8.0"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "f489d0aa1a8b7d3803bf7e7d6c534dc0157926e140519e8d7d22c069c8a8fb9c"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
