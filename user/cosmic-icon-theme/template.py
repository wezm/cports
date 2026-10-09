pkgname = "cosmic-icon-theme"
pkgver = "1.10.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "52625bef1b83ba2b08afe58197573738d72fb4d316de9d99eac34806a4cae80c"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
