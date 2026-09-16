pkgname = "cargo-bootstrap"
pkgver = "1.97.1"
pkgrel = 0
# satisfy runtime dependencies
hostmakedepends = ["curl"]
# satisfy revdeps
makedepends = ["sqlite", "zlib-ng-compat"]
depends = ["!cargo"]
pkgdesc = "Bootstrap binaries of Rust package manager"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://repo.casuarina.org/distfiles/cargo-{pkgver}-{self.profile.triplet}.tar.xz"
options = ["!strip"]

match self.profile.arch:
    case "x86_64":
        sha256 = (
            "306eecbd2a9d92870360624f8fd1491344d7b5699de86bb5cdbef96530f90ca3"
        )
    case _:
        broken = f"not yet built for {self.profile.arch}"


def install(self):
    self.install_bin("cargo")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
