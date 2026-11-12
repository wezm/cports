pkgname = "libfaketime"
pkgver = "0.9.13"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "PREFIX=/usr",
]
make_check_target = "test"
make_check_args = ["-j1"]
make_use_env = True
checkdepends = ["bash", "perl"]
# for a date command that supports -d
depends = ["uutils-coreutils"]
pkgdesc = "Modify the system time for a single application"
license = "GPL-2.0-only"
url = "https://github.com/wolfcw/libfaketime"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8e56deeb805682b025107e095f1d94a6ea677472f05824cd475f5c5e6e1a5ddf"
options = ["linkundefver"]
