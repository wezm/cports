pkgname = "cosmic-icon-theme"
pkgver = "1.0.13"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d826e222564c1638702b31bce7e95f4cce537d340ff0eee7d91fa4ae84e30c1d"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
