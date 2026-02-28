pkgname = "uchardet"
pkgver = "0.0.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Encoding detector library"
license = "MPL-1.1"
url = "https://www.freedesktop.org/wiki/Software/uchardet"
source = f"$(FREEDESKTOP_SITE)/uchardet/releases/uchardet-{pkgver}.tar.xz"
sha256 = "e97a60cfc00a1c147a674b097bb1422abd9fa78a2d9ce3f3fdcc2e78a34ac5f0"


@subpackage("uchardet-devel")
def _(self):
    return self.default_devel()


@subpackage("uchardet-progs")
def _(self):
    return self.default_progs()
