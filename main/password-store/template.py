pkgname = "password-store"
pkgver = "1.7.4"
pkgrel = 2
build_style = "makefile"
make_install_args = ["WITH_ALLCOMP=yes"]
make_check_target = "test"
depends = ["bash", "git", "gnupg", "tree", "ugetopt"]
checkdepends = [*depends]
pkgdesc = "Console-based password manager"
license = "GPL-2.0-or-later"
url = "https://www.passwordstore.org"
source = f"https://git.zx2c4.com/password-store/snapshot/password-store-{pkgver}.tar.xz"
sha256 = "4c2d0a8b99df8915a87099607a8d912fd05d30651b6f014745c14e4ca8dbbfb7"


def build(self):
    pass
