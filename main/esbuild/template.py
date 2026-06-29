pkgname = "esbuild"
pkgver = "0.28.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/esbuild"]
hostmakedepends = ["go", "nodejs"]
pkgdesc = "JavaScript and CSS bundler and minifier"
license = "MIT"
url = "https://esbuild.github.io"
source = f"https://github.com/evanw/esbuild/archive/v{pkgver}.tar.gz"
sha256 = "65c756fa87d43178ac4a5242454c2bd0fde325f8ecf77997f8fa4b88f94d5cd2"


def post_build(self):
    self.do(
        "node", "scripts/esbuild.js", "npm/esbuild/package.json", "--version"
    )
    self.do("node", "scripts/esbuild.js", "./build/esbuild", "--neutral")


def post_install(self):
    self.install_dir("usr/lib/node_modules/esbuild/bin")

    self.install_file(
        "npm/esbuild/package.json", "usr/lib/node_modules/esbuild"
    )
    self.install_files("npm/esbuild/lib", "usr/lib/node_modules/esbuild")

    self.install_link(
        "usr/lib/node_modules/esbuild/bin/esbuild", "../../../../bin/esbuild"
    )

    self.install_license("LICENSE.md")
