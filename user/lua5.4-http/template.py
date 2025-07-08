pkgname = "lua5.4-http"
pkgver = "0.4"
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
	#  depends=('lua-cqueues'
	#           'lua-luaossl'
	#           'lua-basexx'
	#           'lua-binaryheap'
	#           'lua-lpeg'
	#           'lua-lpeg-patterns'
	#           'lua-fifo')
	#  optdepends=('lua-zlib: gzip compression'
	#              'lua-psl: public suffix list checking')

]
pkgdesc = "Lua continuation queues"
license = "MIT"
url = "https://github.com/daurnimator/lua-http"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d2e3cb9bc04cab70ac4f19351bc74b0dcd8b16cfc2563aa77256eb3a43b3b9e0"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
