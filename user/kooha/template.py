pkgname = "kooha"
pkgver = "2.3.2"
pkgrel = 0
build_style = "meson"
# requires meson 1.12
# cargo-test requires resources to be installed; tries to init gtk
# make_check_args = ["--exclude", "cargo-clippy", "--exclude", "cargo-test"]
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "gst-plugins-base-devel",
    "libadwaita-devel",
    "rust-std",
]
depends = [
    "gst-plugins-base",
    "pipewire-gstreamer",
    "xdg-desktop-portal",
]
pkgdesc = "Screen recorder"
license = "GPL-3.0-or-later"
url = "https://github.com/SeaDve/Kooha"
source = f"{url}/releases/download/v{pkgver}/kooha-{pkgver}.tar.xz"
sha256 = "a8f7d0d6fc1418264639a42833d66866475ed0d30b6f1f50b0b430c7d35b3969"
# as above
options = ["!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile.triplet}/release/kooha")
