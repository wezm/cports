pkgname = "wild"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    # integration tests use gcc
    "--lib",
    # these tests ends up checking vendored files and failing
    "--",
    "--skip",
    "tidy_tests::check_text_files",
    "--skip",
    "tidy_tests::check_toml_format",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Fast linker"
license = "Apache-2.0 OR MIT"
url = "https://github.com/wild-linker/wild"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "99ec83404558d4d0cbde9dd44b8c6fa2a511a2f8bb04a31f54c0929ec4491990"


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/wild")
    self.install_license("LICENSE-MIT")
