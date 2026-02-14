pkgname = "gn"
pkgver = "0_git20260204"
pkgrel = 0
_gitrev = "304bbef6c7e9a86630c12986b99c8654eb7fe648"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
source = f"https://ftp.octaforge.org/q66/random/gn-{_gitrev}.tar.gz"
sha256 = "d9b7774fe787e63cee6c13527572748f9a68ef8132283bc089dc64b6bd2f8fdf"
hardening = ["vis", "cfi"]


def configure(self):
    self.do(
        "python",
        "./build/gen.py",
        "--no-last-commit-position",
        "--no-static-libstdc++",
        "--no-strip",
        "--allow-warnings",
    )


def build(self):
    self.do("ninja", f"-j{self.make_jobs}", "-C", "out")


def check(self):
    self.do("./out/gn_unittests")


def install(self):
    self.install_license("LICENSE")
    self.install_bin("out/gn")
