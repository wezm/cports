pkgname = "cosmic-wallpapers"
pkgver = "1.0.11"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "8b044e2bedd17a3e617878d3521bc451a2c804e73eb6749a18f6edc8e6257c3e"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
