pkgname = "nilfs-utils"
pkgver = "2.2.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-selinux"]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "linux-headers",
    "util-linux-blkid-devel",
    "util-linux-mount-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "Userspace utilities for the NILFS filesystem"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://nilfs.sourceforge.io/en/index.html"
source = f"https://github.com/nilfs-dev/nilfs-utils/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0e9fe51dfb1af0a7d196d1f862795f6aa903bcd061c16273ad557bc48b2db7e8"


@subpackage("nilfs-utils-devel")
def _(self):
    return self.default_devel()
