pkgname = "cosmic-osk"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel", "udev-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC on-screen keyboard"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-osk"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "7d92c3df124d1d009ae94cc95915c9085af4ceeb6027473fc02ee564dcead81a"
# no tests
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "cosmic-osk"))
