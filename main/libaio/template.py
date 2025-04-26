pkgname = "libaio"
pkgver = "0.3.113"
pkgrel = 0
build_style = "makefile"
make_check_target = "partcheck"  # full check needs root, e2fsprogs, mount, etc
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Linux-native asynchronous I/O facility"
license = "LGPL-2.1-or-later"
url = "https://pagure.io/libaio"
source = f"{url}/archive/libaio-{pkgver}/libaio-libaio-{pkgver}.tar.gz"
sha256 = "716c7059703247344eb066b54ecbc3ca2134f0103307192e6c2b7dab5f9528ab"
hardening = ["!ssp"]
# maybe filled in later
options = []

if self.profile().arch == "x86":
    # fails:
    # Starting cases/20.p
    # aio_max_nr: 65536
    # Creating 65536 ioctx-s with 1 events each...
    # Killed
    options += ["!check"]


@subpackage("libaio-devel")
def _(self):
    return self.default_devel()
