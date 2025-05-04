# nb: requires CXX14+ to use it
pkgname = "gtest"
pkgver = "1.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_SKIP_INSTALL_RPATH=ON",
    "-Dgmock_build_tests=ON",
    "-Dgtest_build_tests=ON",
]
if self.profile().arch == "x86":
    # fails on x86 with differing floating point stringification
    # PrintOptionalTest.Basic
    # PrintBuiltInTypeTest.FloatingPoints
    make_check_args = [
        "-E",
        "(googletest-port-test|googletest-printers-test)",
    ]
else:
    make_check_args = []
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
pkgdesc = "Google's framework for writing C++ tests"
license = "BSD-3-Clause"
url = "https://github.com/google/googletest"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "78c676fc63881529bf97bf9d45948d905a66833fbfa5318ea2cd7478cb98f399"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("gtest-devel")
def _(self):
    return self.default_devel()
