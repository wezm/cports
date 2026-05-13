pkgname = "cosmic-wallpapers"
pkgver = "1.0.13"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "aac6ccfe37e38505078859981ff2d59ce66497b61c36f055a2af1c64ca27dc91"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
