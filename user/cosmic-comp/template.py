pkgname = "cosmic-comp"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "libdisplay-info-devel",
    "libinput-devel",
    "libseat-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "oniguruma-devel",
    "pixman-devel",
    "rust-std",
    "udev-devel",
    "wayland-devel",
    "zstd-devel",
]
depends = ["cosmic-icon-theme"]
pkgdesc = "COSMIC compositor"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-comp"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "56fdf357a44f5138cab6fe9599d74a2bba3f5995b7155dd88c13e4f4c9e2cafd"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-comp")
    self.install_file(
        "data/keybindings.ron",
        "usr/share/cosmic/com.system76.CosmicSettings.Shortcuts/v1",
        name="defaults",
    )
    self.install_file(
        "data/tiling-exceptions.ron",
        "usr/share/cosmic/com.system76.CosmicSettings.WindowRules/v1",
        name="tiling_exception_defaults",
    )
