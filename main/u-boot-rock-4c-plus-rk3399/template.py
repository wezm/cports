pkgname = "u-boot-rock-4c-plus-rk3399"
pkgver = "2025.04"
pkgrel = 0
archs = ["aarch64"]
build_style = "u_boot"
make_build_args = [
    "BL31="
    + str(
        self.profile().sysroot / "usr/lib/trusted-firmware-a/rk3399/bl31.elf"
    ),
]
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-aarch64-none-elf",
    "gnutls-devel",
    "openssl3-devel",
    "python-devel",
    "python-pyelftools",
    "python-setuptools",
    "swig",
    "util-linux-uuid-devel",
]
makedepends = ["atf-rk3399-bl31"]
pkgdesc = "U-Boot for Radxa ROCK 4C+"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
_ddr_ver = "1.30"
source = [
    f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2",
    f"!https://github.com/rockchip-linux/rkbin/raw/refs/heads/master/bin/rk33/rk3399_ddr_933MHz_v{_ddr_ver}.bin>ddr-v{_ddr_ver}.bin",
]
sha256 = [
    "439d3bef296effd54130be6a731c5b118be7fddd7fcc663ccbc5fb18294d8718",
    "aab3b04166c098c8ba1d9a734c509cdf75b47b64c37c49196c7242526ce32179",
]
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "idbloader.img:64 u-boot.itb:16384",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]


def post_extract(self):
    self.cp(self.sources_path / f"ddr-v{_ddr_ver}.bin", ".")


def init_build(self):
    self.make_build_args += [f"ROCKCHIP_TPL=ddr-v{_ddr_ver}.bin"]

