pkgname = "musl-crypt"
pkgver = "1.2.5_git20260312"
pkgrel = 0
_commit = "1b76ff0767d01df72f692806ee5adee13c67ef88"
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
configure_gen = []
make_build_target = "crypt-libs"
make_install_target = "install-crypt"
hostmakedepends = ["pkgconf"]
replaces = ["libxcrypt"]
pkgdesc = "Crypt library extracted from musl libc"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
]
sha256 = [
    "9b165352849f8203668b8057fec53e2670a4c2261c932fafa0b47795963917a6",
]
# does not ship tests
options = ["!check"]


def post_install(self):
    self.install_file("libcrypt.pc", "usr/lib/pkgconfig")

    self.install_link("usr/lib/libcrypt.so.2", "libcrypt.so.2.0.0")
    self.install_link("usr/lib/libcrypt.so", "libcrypt.so.2.0.0")

    self.install_license("COPYRIGHT")


@subpackage("musl-crypt-devel")
def _(self):
    return self.default_devel()
