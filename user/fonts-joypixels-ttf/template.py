pkgname = "fonts-joypixels-ttf"
pkgver = "9.0.0"
pkgrel = 0
pkgdesc = "Emoji font"
license = "custom:joypixels"
url = "https://www.joypixels.com"
source = [
    f"!https://cdn.joypixels.com/distributions/gentoo-linux/font/{pkgver}/joypixels-android.ttf",
    "!https://cdn.joypixels.com/free-license.pdf",
]
source_paths = [".", "."]
sha256 = [
    "a661ac5606122bf7393a584e5e1365441b3f5e9a4c5e6b0771979298892e103e",
    "b8572500ff2ff25387c9a1f51f2f122215a881ebcf723adddf09fa347b3e64e6",
]


def install(self):
    self.install_license(self.sources_path / "free-license.pdf")
    self.install_file(
        self.sources_path / "joypixels-android.ttf",
        "usr/share/fonts/joypixels",
        name="JoyPixels.ttf",
    )
