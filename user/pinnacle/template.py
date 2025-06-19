pkgname = "pinnacle"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cargo"
# skip integration tests that fail
make_check_args = [
    "--",
    "--skip",
    "tag_v1",
    "--skip",
    "window_v1",
    "--skip",
    "output_v1",
    "--skip",
    "pinnacle_v1",
]
hostmakedepends = ["cargo-auditable", "protobuf-protoc", "pkgconf"]
makedepends = [
    "rust-std",
    "libxkbcommon-devel",
    "udev-devel",
    "libseat-devel",
    "libdisplay-info-devel",
    "libinput-devel",
    "mesa-gbm-devel",
    "lua5.4-devel",
]
pkgdesc = "Tiling Wayland compositor"
license = "GPL-3.0-or-later"
url = "https://github.com/pinnacle-comp/pinnacle"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9002dd4caa8ab8d7831a8e66f449e535a8bfef6b04eeac9afd98ca1e4b5a3fb4"
# cross: generates completions using host binary
options = ["!cross"]


def post_extract(self):
    # all tests fail with error:
    # Environment variable XDG_RUNTIME_DIR is not set or invalid
    self.rm("tests/end_to_end.rs")


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"pinnacle.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/pinnacle",
                "gen-completions",
                "--shell",
                shell,
                stdout=f,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/pinnacle")
    self.install_file(
        "resources/pinnacle.desktop", "usr/share/wayland-sessions"
    )
    self.install_file(
        "resources/pinnacle-portals.conf", "usr/share/xdg-desktop-portal"
    )
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"pinnacle.{shell}", shell, "pinnacle")
