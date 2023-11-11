pkgname = "onagre"
pkgver = "1.0.0_alpha0"
_pkgver = "1.0.0-alpha.0"
pkgrel = 0
build_style = "cargo"
# disable the default use-jemalloc and completions features
#  make_build_args = ["-p", ""]
#  make_install_args = ["-p", ""]
#  make_check_args = ["-p", ""]
hostmakedepends = ["cargo"]
makedepends = ["rust-std", "freetype-devel", "fontconfig-devel", "libexpat-devel", "pkgconf"]
depends = ["pop-launcher"]
pkgdesc = "Application launcher for X and wayland"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/oknozor/onagre"
source = f"{url}/archive/{_pkgver}.tar.gz"
sha256 = "a5285ba87ac6fd836c59e9facd167f5a0a5741630572e783f6aafacb835ca975"


def post_install(self):
    self.install_license("LICENSE")
    #self.install_man("doc/fd.1", "fd.1")
    #self.install_completion("contrib/completion/_fd", "zsh")
