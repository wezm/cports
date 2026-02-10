# in general do not use this; look if it can be patched for libedit first
# there are APIs in readline that are not provided by libedit (usually
# really bad ones) and sometimes we cannot just replace it
pkgname = "readline"
pkgver = "8.3.001"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-multibyte",
    "--with-curses",
    "bash_cv_termcap_lib=libncursesw",
]
# broken af
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel"]
pkgdesc = "GNU Readline library"
license = "GPL-3.0-or-later"
url = "https://tiswww.cwru.edu/php/chet/readline/rltop.html"
source = "$(GNU_SITE)/readline/readline-8.3.tar.gz"
sha256 = "fe5383204467828cd495ee8d1d3c037a7eba1389c22bc6a041f627976f9061cc"


def post_install(self):
    self.uninstall("usr/share/doc")


@subpackage("readline-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])
