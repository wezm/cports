pkgname = "aws-vault"
pkgver = "7.10.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
# makedepends = ["ncurses-devel"]
pkgdesc = "Vault for storing and accessing AWS credentials"
license = "MIT"
url = "https://github.com/ByteNess/aws-vault"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "15521e9ee4246dbc66d250f042939b8c33264c9502162c9bf1318b335966352c"


def post_install(self):
    with self.pushd("contrib/completions"):
        for shell in ["bash", "fish", "zsh"]:
            self.install_completion(f"{shell}/aws-vault.{shell}", shell)

    self.install_license("LICENSE")
