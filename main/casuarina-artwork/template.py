pkgname = "casuarina-artwork"
pkgver = "0.2.0"
pkgrel = 0
pkgdesc = "Casuarina Linux artwork"
license = "CC-BY-4.0"
url = "https://casuarina.org"
source = (
    f"https://codeberg.org/casuarina/casuarina-artwork/archive/{pkgver}.tar.gz"
)
sha256 = "09f01dbc77c97dc39cf657d850038660939c7c98b40c9cf760f16aa4812a881b"


def install(self):
    dp = "usr/share/backgrounds/casuarina"
    self.install_file("wallpaper/casuarina-ocean.jpg", dp, name="bg-l.jpg")
    self.install_file(
        self.files_path / "casuarina.xml",
        "usr/share/gnome-background-properties",
    )

    # KDE
    self.install_dir("usr/share/wallpapers/Casuarina/contents/images")
    self.install_dir("usr/share/wallpapers/Casuarina/contents/images_dark")
    self.install_file(
        "breeze-previews/metadata.json", "usr/share/wallpapers/Casuarina"
    )
    self.install_link(
        "usr/share/wallpapers/Casuarina/contents/images/6016x4011.jpg",
        "../../../../backgrounds/casuarina/bg-l.jpg",
    )
    self.install_link(
        "usr/share/wallpapers/Casuarina/contents/images_dark/6016x4011.jpg",
        "../../../../backgrounds/casuarina/bg-l.jpg",
    )

    for theme in ["breeze", "breezedark", "breezetwilight"]:
        previews_path = f"usr/share/plasma/look-and-feel/org.kde.{theme}.desktop/contents/previews"
        self.install_dir(previews_path)
        self.install_file(
            f"breeze-previews/{theme}-preview.png",
            previews_path,
            name="preview.png",
        )
        self.install_file(
            f"breeze-previews/{theme}-fullscreenpreview.jpg",
            previews_path,
            name="fullscreenpreview.jpg",
        )


@subpackage("casuarina-artwork-kde")
def _(self):
    self.subdesc = "KDE files"
    self.replaces = ["plasma-workspace<6.1.1-r1"]

    return ["usr/share/plasma", "usr/share/wallpapers"]
