pkgname = "aws-vault"
pkgver = "7.18.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
# makedepends = ["ncurses-devel"]
pkgdesc = "Vault for storing and accessing AWS credentials"
license = "MIT"
url = "https://github.com/ByteNess/aws-vault"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "957408bf9337e42d20f2c98958c7dfb20272072653c88ccc6c2d39650a084ced"


def post_install(self):
    with self.pushd("contrib/completions"):
        for shell in ["bash", "fish", "zsh"]:
            self.install_completion(f"{shell}/aws-vault.{shell}", shell)

    self.install_license("LICENSE")
