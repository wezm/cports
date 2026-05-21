pkgname = "cargo-c"
pkgver = "0.10.22"
pkgrel = 0
build_style = "cargo"
# no tests in others
make_check_args = ["--lib"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "libgit2-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Cargo plugin to install C-ABI libraries"
license = "MIT"
url = "https://github.com/lu-zero/cargo-c"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock>Cargo.lock.{pkgver}",
]
source_paths = [".", "."]
sha256 = [
    "a7b00539437932f2a17a72b97d9c2142367a2d70ee20f9f1692a8b13c7255332",
    "f7837bca0bda930b3007e08e740f3ee9482796e349c05af25ded58c81cfd8db3",
]
# mfs be like rebuild literally everything and then run
# test_semver_one_zero_zero and test_semver_zero_zero_zero
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


def post_install(self):
    self.install_license("LICENSE")
