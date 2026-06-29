pkgname = "aws-vault"
pkgver = "7.12.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
# makedepends = ["ncurses-devel"]
pkgdesc = "Vault for storing and accessing AWS credentials"
license = "MIT"
url = "https://github.com/ByteNess/aws-vault"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f1c5ae09608bfb16b1724089e0bcebe4bc56fc93037dc80245759d7ac88144c2"


def post_install(self):
    with self.pushd("contrib/completions"):
        for shell in ["bash", "fish", "zsh"]:
            self.install_completion(f"{shell}/aws-vault.{shell}", shell)

    self.install_license("LICENSE")
