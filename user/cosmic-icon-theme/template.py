pkgname = "cosmic-icon-theme"
pkgver = "1.9.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "1b15f26b5a6b876aaeb82fd51c1bf242b2c26bb5899105dd03168feba4896ae5"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
