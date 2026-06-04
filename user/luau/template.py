pkgname = "luau"
pkgver = "0.723"
pkgrel = 0
build_style = "cmake"
configure_args = ["-D LUAU_BUILD_TESTS=On"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Gradually typed embeddable scripting language derived from Lua"
license = "MIT"
url = "https://luau.org"
source = f"https://github.com/luau-lang/luau/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "74bf6b8842e00d236d390f9431205c73d0cf887c973f9d0656396bbf1eb987bd"


def check(self):
    self.do("build/Luau.Conformance")
    self.do("build/Luau.UnitTest")


def install(self):
    for bin in [
        "luau",
        "luau-analyze",
        "luau-ast",
        "luau-bytecode",
        "luau-compile",
        "luau-reduce",
    ]:
        self.install_bin(f"build/{bin}")

    self.install_license("LICENSE.txt")
    self.install_license("lua_LICENSE.txt")
    self.install_license("extern/isocline/LICENSE", "isocline-LICENSE")
