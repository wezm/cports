pkgname = "cosmic-wallpapers"
pkgver = "1.3.0"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "5fac81715b6e4dd11a4b561761da075f3d3d72c45714aa4312d1617be21edc98"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
