pkgname = "libfaketime"
pkgver = "0.9.10"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "PREFIX=/usr",
]
make_install_args = [
    "PREFIX=/usr",
]
make_use_env = True
#  make_check_target = "test"
#  make_check_args = ["-j1"]
pkgdesc = "Report fake dates and times to programs"
license = "GPL-2.0-or-later"
url = "https://github.com/wolfcw/libfaketime"
source = f"https://github.com/wolfcw/libfaketime/archive/v{pkgver}/libfaketime-{pkgver}.tar.gz"
sha256 = "729ad33b9c750a50d9c68e97b90499680a74afd1568d859c574c0fe56fe7947f"
tool_flags = {"CFLAGS": ["-D_LARGEFILE64_SOURCE"]}

# https://github.com/wolfcw/libfaketime/issues/259
options = ["!check", "!lto"]

#  @subpackage("libfaketime-devel")
#  def _(self):
#      return self.default_devel()

@subpackage("libfaketime-progs")
def _(self):
    return self.default_progs()
