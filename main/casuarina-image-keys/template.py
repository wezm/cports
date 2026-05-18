pkgname = "casuarina-image-keys"
pkgver = "20260518"
pkgrel = 0
build_style = "meta"
depends = ["minisign"]
pkgdesc = "Casuarina public keys for image verification"
license = "custom:meta"
url = "https://casuarina.org"


def install(self):
    for f in self.files_path.glob("*.pub"):
        self.install_file(f, "usr/share/casuarina-image-keys")
