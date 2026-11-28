pkgname = "tiny-git"
pkgver = "0.13.0_git20261128"
pkgrel = 0
_gitrev = "7c897c2f4cb4be33c4fcd2d0811b6d590e1a6e0d"
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "tls-native,desktop-notifications",
    "--bin",
    "tiny",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["dbus-devel", "openssl3-devel", "rust-std"]
provides = [self.with_pkgver("tiny")]
pkgdesc = "Terminal IRC client"
license = "MIT"
url = "https://github.com/osa1/tiny"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "fa47e36b1b58594a057139afa48e60e06b6f116229606ea6b4def1b0904560b1"

#  if self.profile.arch in ["loongarch64"]:
#      broken = "outdated nix crate, can't update"


def install(self):
    self.cargo.install(wrksrc="crates/tiny")
    self.install_license("LICENSE")
