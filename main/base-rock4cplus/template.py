pkgname = "base-rock4cplus"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = [
    "firmware-linux-brcm",
    "firmware-linux-rockchip",
    "u-boot-rock-4c-plus-rk3399",
    "u-boot-menu",
]
pkgdesc = "Chimera base package for Radxa ROCK 4C+"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    # u-boot-menu
    self.install_file(self.files_path / "device", "usr/lib/u-boot")
    self.install_file(self.files_path / "cmdline", "usr/lib/u-boot")
