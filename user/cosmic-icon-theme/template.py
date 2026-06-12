pkgname = "cosmic-icon-theme"
pkgver = "1.0.16"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "d23aecb6a5586795c2fc0f305c0055b413e788980db1b983705f5eaaa864862c"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
