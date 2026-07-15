pkgname = "cosmic-icon-theme"
pkgver = "1.3.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "b0a4670a8190ca606c57924acc3a0ceb97ccd993f8d159352561729575a2fcc1"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
