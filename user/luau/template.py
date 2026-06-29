pkgname = "luau"
pkgver = "0.727"
pkgrel = 0
build_style = "cmake"
configure_args = ["-D LUAU_BUILD_TESTS=On"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Gradually typed embeddable scripting language derived from Lua"
license = "MIT"
url = "https://luau.org"
source = f"https://github.com/luau-lang/luau/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a03896f1a55887a2d04dcd268f3c049724d728158ae0ac2b0bd749ea7b7b5e5b"


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
