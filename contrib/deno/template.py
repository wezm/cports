pkgname = "deno"
pkgver = "1.35.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gn", "ninja", "llvm", "clang", "python"] # llvm for llvm-ar
makedepends = ["rust"]
pkgdesc = "Runtime for JavaScript and TypeScript"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/denoland/deno"
source = f"{url}/releases/download/v{pkgver}/deno_src.tar.gz"
#https://github.com/denoland/deno/releases/download/v1.35.1/deno_src.tar.gz
sha256 = "2bb20669b45d19102f023b4e63de143d5b552d8bfc03b4c247ca877870949496"

env = {
    # Build V8 from source instead of attemping to download pre-built library
    "V8_FROM_SOURCE": "1",
    # Don't download gn
    "GN": "/usr/bin/gn",
    # Don't download ninja
    "NINJA": "/usr/bin/ninja",
    # Don't download clang
    "CLANG_BASE_PATH": "/usr",
    # Don't build a custom libcxx
    "GN_ARGS": "use_custom_libcxx=false",
}


def post_install(self):
    self.install_license("LICENSE.md")
    #  self.install_man("doc/fd.1", "fd.1")
    #  self.install_completion("contrib/completion/_fd", "zsh")
