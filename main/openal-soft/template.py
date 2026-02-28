pkgname = "openal-soft"
pkgver = "1.25.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DALSOFT_EXAMPLES=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "libpulse-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "sdl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Cross-platform 3D audio API"
license = "LGPL-2.1-or-later"
url = "https://openal-soft.org"
# expired certificate
# source = f"{url}/openal-releases/openal-soft-{pkgver}.tar.bz2"
source = f"https://github.com/kcat/openal-soft/archive/{pkgver}.tar.gz"
sha256 = "5f8efe8dfba5e9307a50251ba615ace857c7fa9dddfe34130b83e213d7f7cf24"
# no test target
options = ["!check"]


def post_install(self):
    self.uninstall("usr/share/openal/alsoftrc.sample")
    self.install_file("alsoftrc.sample", "usr/share/examples/openal-soft")


@subpackage("openal-soft-devel")
def _(self):
    return self.default_devel()
