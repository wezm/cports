pkgname = "cosmic-icon-theme"
pkgver = "1.8.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a85368f132859fcc00ef07304dd8688f9d372b3b83b2b2f39477585e4b9c247b"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
