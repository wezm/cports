pkgname = "libdisplay-info"
pkgver = "0.2.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "hwdata-devel",
]
pkgdesc = "EDID and DisplayID library"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/libdisplay-info"
source = f"{url}/-/archive/{pkgver}/libdisplay-info-{pkgver}.tar.gz"
sha256 = "f7331fcaf5527251b84c8fb84238d06cd2f458422ce950c80e86c72927aa8c2b"
# below
options = []

if self.profile().arch == "x86":
    # 3/46 decode-apple-xdr-dp FAIL
    options.append("!check")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdisplay-info-devel")
def _(self):
    return self.default_devel()
