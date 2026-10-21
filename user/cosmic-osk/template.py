pkgname = "cosmic-osk"
pkgver = "1.11.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel", "udev-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC on-screen keyboard"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-osk"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "bdb94386f451e672c2512ddb65bd0c8691921d5488595d0988fd935ce7e43bb6"
# no tests
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "cosmic-osk"))
