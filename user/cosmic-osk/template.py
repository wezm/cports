pkgname = "cosmic-osk"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "libxkbcommon-devel", "udev-devel"]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC on-screen keyboard"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-osk"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "6a4095f0474d55ecefe0e1f4bb24f5a7bffdf0450e87de40c668da1d628bd1f6"
# no tests
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "cosmic-osk"))
