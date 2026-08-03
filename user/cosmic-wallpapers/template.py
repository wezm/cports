pkgname = "cosmic-wallpapers"
pkgver = "1.5.0"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "decdaf0b17fd1fda7de5adf763bb68ef46c39daae1bd627330f66cf1a679b99d"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
