pkgname = "openvi"
pkgver = "7.0.11"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
makedepends = ["ncurses-devel", "gmake", "musl-bsd-headers"]
depends = ["ncurses"]
pkgdesc = "Portable OpenBSD vi for UNIX systems"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "BSD-3-Clause"
url = "https://github.com/johnsonjh/OpenVi"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d1bb1bf56bbc644ad9f95ed1b5a3ac4e46f0808a7e983f0967ca519afa7edff1"

# no tests
options = ["!check"]

def do_install(self):
    self.install_bin("bin/vi")
    self.install_link("vi", "usr/bin/view")
    self.install_link("vi", "usr/bin/ex")
    self.install_file("scripts/virecover", "usr/libexec", name = "vi.recover")
    self.install_man("docs/USD.doc/vi.man/vi.1")
    self.install_man("scripts/virecover.8", "vi.recover.8")
    self.install_dir("var/tmp/vi.recover", mode = 0o1777, empty = True)
    self.install_license("LICENSE.md")

