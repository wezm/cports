pkgname = "espanso-wayland"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "wayland,modulo,vendored-tls",
]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "libcap-progs", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "libxkbcommon-devel",
    "rust-std",
    "turnstile",
    "wxwidgets-devel",
    "wxwidgets-gtk3",
]
depends = ["wl-clipboard"]
pkgdesc = "Automatic ZFS snapshot utility"
license = "GPL-3.0-only"
url = "https://espanso.org"
source = f"https://github.com/espanso/espanso/archive/v{pkgver}.tar.gz"
sha256 = "90895a8a79476f902a6cfc88a67e8e077971be13f728ce1a35866355d60285a7"
env = {"CXXSTDLIB": "c++"}
file_modes = {
    "usr/bin/espanso": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/espanso": {
        "security.capability": "cap_dac_override+p",
    }
}


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/espanso")
    self.install_file(
        "espanso/src/res/linux/espanso.desktop", "usr/share/applications"
    )
    self.install_file(
        "espanso/src/res/linux/icon.png",
        "usr/share/icons/hicolor/160x160/apps/espanso.png",
        name="espanso.png",
    )
    self.install_service(self.files_path / "espanso.user")
