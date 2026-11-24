pkgname = "titlecase"
pkgver = "3.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Tool for transforming text into title case"
license = "MIT"
url = "https://github.com/wezm/titlecase"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d73fac5fcba3046cf23afe260bb2c58b4878d5b9d06830c0d8ebe22b01eb8d4f"


def post_install(self):
    self.install_license("LICENSE")
