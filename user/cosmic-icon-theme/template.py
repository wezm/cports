pkgname = "cosmic-icon-theme"
pkgver = "1.0.15"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "f0745b25285cae94ae1a61e7fd700234342d5fc871150725afc06a7f271d4c0f"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
