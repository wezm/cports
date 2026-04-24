pkgname = "pop-sound-theme"
pkgver = "5.3.1_git20260424"
pkgrel = 0
_commit = "25ea85d97126992024b03bfb4e4c3b0711c749ed"
pkgdesc = "Pop OS sound theme"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/gtk-theme"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "956897202a6e3543ad0f11b44fb49e2e4a8a6613be85e0850ca7024bf5b8a2f9"


def install(self):
    self.install_file(
        "sounds/src/index.theme.in", "usr/share/sounds/Pop", name="index.theme"
    )
    self.install_files("sounds/src/stereo", "usr/share/sounds/Pop")
