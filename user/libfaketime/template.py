pkgname = "libfaketime"
pkgver = "0.9.12"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "PREFIX=/usr",
]
make_check_target = "test"
make_use_env = True
checkdepends = ["bash", "perl"]
# for a date command that supports -d
depends = ["uutils-coreutils"]
pkgdesc = "Modify the system time for a single application"
license = "GPL-2.0-only"
url = "https://github.com/wolfcw/libfaketime"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4fc32218697c052adcdc5ee395581f2554ca56d086ac817ced2be0d6f1f8a9fa"
options = ["linkundefver"]
