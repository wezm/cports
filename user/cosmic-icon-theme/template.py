pkgname = "cosmic-icon-theme"
pkgver = "1.6.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "07bd13f76da382d859aafe9609e69b92665da46255b6273ad5c801c7d344196d"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
