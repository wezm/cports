pkgname = "fetsh"
pkgver = "0_git20261022"
pkgrel = 0
_gitrev = "6d162a232e9e03d2971426475880d9d6f489389e"
_token = self.get_data("codeberg_token")
build_style = "meson"
hostmakedepends = ["meson"]
# makedepends = ["dinit-chimera", "linux-headers", "zstd-devel"]
pkgdesc = "System information tool"
license = "GPL-3.0-only"
url = "https://codeberg.org/wezm/fetsh"
# https://codeberg.org/wezm/fetsh/archive/6d162a232e9e03d2971426475880d9d6f489389e.tar.gz
source = f"https://codeberg.org/api/v1/repos/wezm/fetsh/archive/{_gitrev}.tar.gz>fetsh-{pkgver}.tar.gz"
source_headers = {
    "Authorization": f"Bearer {_token}",
}
sha256 = "7f7850d65e156477b8ad6ca654f15a5f632d43bda0b16339f5d311b9dfd70289"
