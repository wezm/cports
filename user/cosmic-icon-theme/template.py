pkgname = "cosmic-icon-theme"
pkgver = "1.0.8"
pkgrel = 0
hostmakedepends = ["just"]
depends = ["pop-icon-theme"]
pkgdesc = "COSMIC icon theme"
license = "CC-BY-SA-4.0"
url = "https://github.com/pop-os/cosmic-icons"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "4fc8d208316532766de8c4481b88e8a28fb42cdcb184ef4c92393dad1c98367c"


def install(self):
    self.do("just", f"rootdir={self.chroot_destdir}", "install")
