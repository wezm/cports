pkgname = "lua5.4-protobuf"
pkgver = "0.5.3"
pkgrel = 0
build_style = "makefile"
make_build_args = ["LUA_VERSION=5.4"]
make_install_args = ["LUA_VERSION=5.4"]
makedepends = ["lua5.4-devel"]
pkgdesc = "Protobuf module for Lua"
license = "MIT"
url = "https://github.com/starwing/lua-protobuf"
source=(f"{url}/archive/{pkgver}.tar.gz")
sha256 = "54feb9c48e13304e50a4177976b66c1ad395364c500bf00cbf9e3cb59c36ed91"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")

