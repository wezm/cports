pkgname = "u-boot-nezha"
pkgver = "2022.10"
pkgrel = 0
_tag = "d1-2022-10-31"
archs = ["riscv64"]
build_style = "u_boot"
make_build_args = ["OPENSBI=/usr/lib/opensbi/generic/fw_dynamic.bin"]
hostmakedepends = [
    "gmake",
    "gcc-riscv64-unknown-elf",
    "flex",
    "bison",
    "dtc",
    "swig",
    "opensbi",
    "python-devel",
    "openssl-devel",
    "python-setuptools",
]
pkgdesc = "U-Boot for Allwinner D1 boards"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://github.com/smaeul/u-boot/archive/refs/tags/{_tag}.tar.gz"
sha256 = "8bb3694533e66d3d233c62447a7f7dd031eb7ff328e2760b288be71de90d3f21"
env = {
    "DEVICE_TREE": "sun20i-d1-mangopi-mq-pro",
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot-sunxi-with-spl.bin u-boot.itb",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]
