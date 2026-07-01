pkgname = "cosmic-icon-theme"
pkgver = "1.2.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "e86484a3d8bd2bf15db9924a92741ca31a557ee49f59822fb2c1686316287f7e"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
