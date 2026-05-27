pkgname = "cosmic-icon-theme"
pkgver = "1.0.14"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "839ace955920191fc80cc3fe2ef1c5bb1d15c0c149082b61ab3217eac09e10ed"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
