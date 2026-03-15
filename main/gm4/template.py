pkgname = "gm4"
pkgver = "1.4.20"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-changeword",
    "--enable-threads",
    "--program-prefix=g",
    # "ac_cv_lib_error_at_line=no",
    # "ac_cv_header_sys_cdefs_h=no",
]
# cyclic as autotools needs gm4
configure_gen = []
hostmakedepends = ["texinfo"]
pkgdesc = "GNU version of UNIX m4 macro language processor"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/m4"
source = f"$(GNU_SITE)/m4/m4-{pkgver}.tar.xz"
sha256 = "e236ea3a1ccf5f6c270b1c4bb60726f371fa49459a8eaaebc90b216b328daf2b"
# CFI: there is something wrong with oset vtable
hardening = ["vis", "!cfi"]
options = ["bootstrap"]
