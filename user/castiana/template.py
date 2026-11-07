pkgname = "castiana"
pkgver = "0.1.0_pre2"
pkgrel = 0
_gitrev = "24ab3d0"
_token = self.get_data("codeberg_token")
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "lua5.5-devel"]
pkgdesc = "Web runtime for Fennel"
license = "custom:none"
url = "https://codeberg.org/wezm/castiana"
source = f"https://codeberg.org/api/v1/repos/wezm/castiana/archive/{_gitrev}.tar.gz>castiana-{pkgver}.tar.gz"
source_headers = {
    "Authorization": f"Bearer {_token}",
}
sha256 = "b5d9401607a97d89da99850b5da4cf58a5043467cd16e7b92e9b204a4b3a94aa"
