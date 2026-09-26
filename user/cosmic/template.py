pkgname = "cosmic"
pkgver = "1.9.0"
pkgrel = 0
build_style = "meta"
depends = [
    "cosmic-initial-setup",
    "cosmic-session",
]
pkgdesc = "COSMIC desktop environment"
license = "custom:meta"
url = "https://www.gnome.org"


@subpackage("cosmic-apps")
def _(self):
    self.subdesc = "apps"
    self.install_if = [self.parent]
    self.depends = [
        "cosmic-edit",
        "cosmic-monitor",
        "cosmic-player",
        # "cosmic-reader",
        "cosmic-term",
        "cosmic-viewer",
    ]
    return []
