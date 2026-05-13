pkgname = "xdg-desktop-portal-cosmic"
pkgver = "1.0.13"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "glib-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "pipewire-devel",
    "rust-std",
    "wayland-devel",
    "zstd-devel",
]
checkdepends = [
    "gstreamer-devel",
]
depends = ["cosmic-icon-theme", "xdg-desktop-portal"]
pkgdesc = "Backend implementation for xdg-desktop-portal using libcosmic"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/xdg-desktop-portal-cosmic"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "78c8d4d85ebfc8810ed1cae686290f9217405ae78aecc4b7bf26bdbd86bf2caa"
# no tests
options = ["!check"]


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/xdg-desktop-portal-cosmic",
        "usr/lib",
    )
    self.install_file(
        "data/dbus-1/org.freedesktop.impl.portal.desktop.cosmic.service.in",
        "usr/share/dbus-1/services",
        name="org.freedesktop.impl.portal.desktop.cosmic.service",
    )
    self.install_file(
        "data/cosmic.portal", "usr/share/xdg-desktop-portal/portals"
    )
    self.install_file(
        "data/cosmic-portals.conf", "usr/share/xdg-desktop-portal"
    )
    default_schema = self.cwd / "data/icons"
    # TODO: Maybe put these in a cosmic subdir
    for p in default_schema.iterdir():
        if p.is_dir():
            self.install_files(p, "usr/share/icons/hicolor")
