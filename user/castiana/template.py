pkgname = "castiana"
pkgver = "0.1.0"
pkgrel = 1
_gitrev = "92f7a99"
_token = self.get_data("codeberg_token")
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "lua5.4-devel"]
pkgdesc = "Web runtime for Fennel"
license = "custom:none"
url = "https://codeberg.org/wezm/castiana"
source = f"https://codeberg.org/api/v1/repos/wezm/castiana/archive/{_gitrev}.tar.gz>castiana-{pkgver}.tar.gz"
source_headers = {
    "Authorization": f"Bearer {_token}",
}
sha256 = "070d5b5c59f9eb0aad2a3bbdeb79fd87890eb8d4b02fac32da8cca0e63781968"
