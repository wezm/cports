pkgname = "gleam"
pkgver = "1.15.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
checkdepends = ["erlang", "git", "nodejs"]
depends = ["erlang"]
pkgdesc = "Friendly language for building scalable type-safe systems"
license = "Apache-2.0"
url = "https://gleam.run"
source = (
    f"https://github.com/gleam-lang/gleam/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6fe365a52660d854a73d56e0752fc9ff47fdaa19b0ddc9edbcaa1fb935685eca"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
