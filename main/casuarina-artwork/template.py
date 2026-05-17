pkgname = "casuarina-artwork"
pkgver = "0.1.0"
pkgrel = 0
pkgdesc = "Casuarina Linux artwork"
license = "CC-BY-4.0"
url = "https://casuarina.org"
source = (
    f"https://codeberg.org/casuarina/casuarina-artwork/archive/{pkgver}.tar.gz"
)
sha256 = "65d77130eedce695c148b854108b1d1a2d00cd94ef9ed81713934a471e8d5f49"


def install(self):
    dp = "usr/share/backgrounds/casuarina"
    self.install_file("wallpaper/casuarina-ocean.jpg", dp, name="bg-l.jpg")
    self.install_file(
        self.files_path / "casuarina.xml",
        "usr/share/gnome-background-properties",
    )

    # TODO: KDE
