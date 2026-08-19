pkgname = "cosmic-comp"
pkgver = "1.6.0"
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
sha256 = "c3cc440fd5e0f2b3eda42d28a956a7c19616391c52c1c27efd1a002c131d15cc"
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
