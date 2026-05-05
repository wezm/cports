pkgname = "cosmic-comp"
pkgver = "1.0.11"
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
sha256 = "3d4f465f76bfad9e110ef220e2a25917e91e76ea849403a7bb7be41bf2bb34b8"
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
