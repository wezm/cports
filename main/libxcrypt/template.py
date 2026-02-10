pkgname = "libxcrypt"
pkgver = "4.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: perhaps enable fewer hashes
    "--enable-hashes=all",
    "--disable-failure-tokens",
    "--enable-obsolete-api=no",
]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = []
checkdepends = ["python-passlib"]
pkgdesc = "Library for one-way hashing of passwords"
license = "LGPL-2.1-or-later"  # FIXME: verify
url = "https://github.com/besser82/libxcrypt"
source = f"{url}/releases/download/v{pkgver}/libxcrypt-{pkgver}.tar.xz"
sha256 = "71513a31c01a428bccd5367a32fd95f115d6dac50fb5b60c779d5c7942aec071"
# lto: not currently supported
# check: FIXME
# FAIL: test/symbols-static.pl
# FAIL: test/symbols-renames.pl
options = ["!lto", "!check"]


@subpackage("libxcrypt-devel")
def _(self):
    return self.default_devel()
