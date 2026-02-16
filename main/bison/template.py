pkgname = "bison"
pkgver = "3.8.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-yacc"]
hostmakedepends = ["automake", "gettext-devel", "gm4", "perl", "texinfo"]
makedepends = ["gettext-devel"]
checkdepends = ["flex", "autoconf"]
depends = ["gm4"]
pkgdesc = "GNU yacc(1) replacement"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bison"
source = f"$(GNU_SITE)/bison/bison-{pkgver}.tar.xz"
sha256 = "9bba0214ccf7f1079c5d59210045227bcf619519840ebfa80cd3849cff5a5bf2"
hardening = ["vis", "!cfi"]
# FIXME: (fails on master too)
# 764: Leaked lookahead after nondeterministic parse syntax error: glr2.cc FAILED (glr-regression.at:1862)
options = ["bootstrap", "!check"]


def init_configure(self):
    self.configure_args += [
        f"--with-libtextstyle-prefix={self.chroot_destdir}/usr",
    ]
