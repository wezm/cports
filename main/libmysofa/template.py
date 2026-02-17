pkgname = "libmysofa"
pkgver = "1.3.2"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
# tests fail when run in parallel
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["cunit-devel", "zlib-ng-compat-devel"]
checkdepends = []
pkgdesc = "Reader for AES SOFA files to get better HRTFs"
license = "BSD-3-Clause"
url = "https://github.com/hoene/libmysofa"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6c5224562895977e87698a64cb7031361803d136057bba35ed4979b69ab4ba76"
# FIXME: breaks fail-issue-167a test
hardening = ["!int"]
# no nodejs on some platforms
options = []


match self.profile().arch:
    case "aarch64" | "loongarch64" | "ppc64le" | "riscv64" | "x86_64":
        checkdepends += ["nodejs"]
    case _:
        options += ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libmysofa-devel")
def _(self):
    return self.default_devel()
