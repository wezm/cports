pkgname = "espanso"
pkgver = "2.4.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "wayland,modulo,native-tls",
]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "libcap-progs", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "libxkbcommon-devel",
    "linux-headers",
    "openssl3-devel",
    "rust-std",
    "turnstile",
    "wxwidgets-devel",
    "wxwidgets-gtk3",
]
depends = ["wl-clipboard"]
pkgdesc = "Text expansion utility"
license = "GPL-3.0-only"
url = "https://espanso.org"
source = f"https://github.com/espanso/espanso/archive/v{pkgver}.tar.gz"
sha256 = "3121627138be4b1f106b8dfd73fb4b7030ecb44c6a8f4e7628a1174b58e5cfe2"
file_modes = {
    "usr/bin/espanso": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/espanso": {
        "security.capability": "cap_dac_override+p",
    }
}


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/espanso")
    self.install_file(
        "espanso/src/res/linux/espanso.desktop", "usr/share/applications"
    )
    self.install_file(
        "espanso/src/res/linux/espanso.png",
        "usr/share/icons/hicolor/160x160/apps/espanso.png",
        name="espanso.png",
    )
    self.install_service(self.files_path / "espanso.user")
