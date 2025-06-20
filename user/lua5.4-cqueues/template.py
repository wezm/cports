pkgname = "lua5.4-cqueues"
pkgver = "20200726"
pkgrel = 0
build_style = "makefile"
#  make_build_args = ["LUA_VERSION=5.4"]
make_install_args = ["prefix=/usr"]
#make_use_env = True
#  hostmakedepends = ["pkgconf"]
makedepends = [
    "lua5.4-devel",
    "openssl3-devel",
    "musl-bsd-headers",
]
pkgdesc = "Lua continuation queues"
license = "MIT"
url = "http://25thandclement.com/~william/projects/cqueues.html"
source = f"https://github.com/wahern/cqueues/archive/rel-{pkgver}.tar.gz"
sha256 = "9e112edd246da5cfca264314b70325a0b63665cb87a00e45ee3ae4f194000d52"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
