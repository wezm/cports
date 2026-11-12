pkgname = "diffr"
pkgver = "0.1.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
]
makedepends = [
    "rust-std",
]
pkgdesc = "Diff presentation tool"
license = "MIT"
url = "https://github.com/mookid/diffr"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6c5861e5b8f5d798e027fe69cc186452848dc4ae5641326b41b5c160d3e91654"


def init_check(self):
    from cbuild.util import cargo

    self.make_check_env["DIFFR_TESTS_BINARY_PATH"] = cargo.target_path(
        self, "diffr"
    )


def post_install(self):
    self.install_license("LICENSE.txt")
