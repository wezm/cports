pkgname = "fonts-source-sans-vf-otf"
pkgver = "3.052"
pkgrel = 0
pkgdesc = "Sans serif font family for UI environments"
subdesc = "variable font"
license = "OFL-1.1"
url = "https://adobe-fonts.github.io/source-sans"
source = f"https://github.com/adobe-fonts/source-sans/releases/download/{pkgver}R/VF-source-sans-{pkgver}R.zip"
sha256 = "d8e2ac355e06e6a0f0e0a0b1ac0c2451afa707584d7bb9d6b11ef9e4b749904c"
# No license in tarball
options = ["!distlicense"]


def install(self):
    self.install_file("*.otf", "usr/share/fonts/source-sans", glob=True)
