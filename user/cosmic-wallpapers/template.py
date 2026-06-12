pkgname = "cosmic-wallpapers"
pkgver = "1.0.16"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "5a95a9a6fb8be7f37cae093e9274221c86140e7143bc4088e63879d52e8bfd9f"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
