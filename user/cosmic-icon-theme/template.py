pkgname = "cosmic-icon-theme"
pkgver = "1.11.0"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "1cbe6ca6ad3743a26b84ab17d3f7b8e5a885fcbcbb2d071ff0b74bccb5b44a53"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
