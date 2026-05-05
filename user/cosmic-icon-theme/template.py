pkgname = "cosmic-icon-theme"
pkgver = "1.0.11"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "1979dc4124edd79c62ed6d3c613b3bef28efe8404690635a555b1478d1dea1f1"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
