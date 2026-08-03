pkgname = "cosmic-icon-theme"
pkgver = "1.5.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "e6caffc4c93f5afdaae3fbda4f3cc14363d3539cda1b0c5f478d32a8bb141c4c"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
