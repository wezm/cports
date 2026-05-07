pkgname = "cosmic-icon-theme"
pkgver = "1.0.12"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "38e5927fbdc96f401b076ce4d99e67cc2d1b2010f612b47b56d714bfe050a7bb"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
