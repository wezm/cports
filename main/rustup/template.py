pkgname = "rustup"
pkgver = "1.29.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "reqwest-rustls-tls,no-self-update",
    "--bin",
    "rustup-init",
]
make_check_args = [
    "--features",
    "test",
]
hostmakedepends = ["cargo-auditable", "pkgconf", "zstd-devel"]
makedepends = ["rust-std"]
checkdepends = ["curl-devel", "openssl3-devel"]
depends = ["llvm-libgcc-devel"]
pkgdesc = "Rust toolchain manager"
license = "MIT OR Apache-2.0"
url = "https://rustup.rs"
source = [
    f"https://github.com/rust-lang/rustup/archive/refs/tags/{pkgver}.tar.gz"
]
sha256 = ["de73d1a62f4d5409a2f6bdb1c523d8dc08aa6d9d63588db62493c19ca8f8bf55"]
# check: needs a different configuration to what we build with, and fails to build
# cross: uses host binary to generate completions
# lintcomp: completion 'rustup' has no matching command
options = ["!check", "!cross", "!lintcomp"]


def post_build(self):
    # required so that can be invoked as rustup
    self.ln_s(f"target/{self.profile().triplet}/release/rustup-init", "rustup")

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"rustup.{shell}", "w") as outf:
            self.do(
                "./rustup",
                "completions",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rustup-init")
    self.install_license("LICENSE-MIT")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"rustup.{shell}", shell)
