pkgname = "cosmic-icon-theme"
pkgver = "1.1.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "1de684477013b47c0f9757e575ed638bbdcd2ffc30829f8e707f5eeba581233b"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
