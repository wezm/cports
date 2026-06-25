pkgname = "cosmic-settings-daemon"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libinput-devel",
    "libpulse",
    "libxkbcommon-devel",
    "openssl3-devel",
    "pipewire-devel",
    "rust-std",
    "udev-devel",
    "zstd-devel",
]
checkdepends = [
    "gstreamer-devel",
]
depends = [
    "adw-gtk3",
    "alsa-utils",
    "breeze-icons",
    # for loginctl
    "elogind",
    "geoclue",
    "playerctl",
    "pop-sound-theme",
    "wireplumber",
]
pkgdesc = "COSMIC settings daemon"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-settings-daemon"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "adb78c8eb43c0acf79a056100653de30f64f220d8387658dfa16efa22fead523"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/cosmic-settings-daemon"
    )
    # TODO: Internal binary feels like it could go in /usr/lib
    # self.install_file(
    #     f"target/{self.profile().triplet}/release/cosmic-settings-daemon",
    #     "usr/lib",
    # )

    self.install_file(
        "data/system_actions.ron",
        "usr/share/cosmic/com.system76.CosmicSettings.Shortcuts/v1",
        name="system_actions",
    )
    self.install_file(
        "data/polkit-1/rules.d/cosmic-settings-daemon.rules",
        "usr/share/polkit-1/rules.d",
    )
