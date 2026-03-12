pkgname = "psmisc"
pkgver = "23.7"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["gettext-devel", "automake"]
makedepends = ["ncurses-devel", "linux-headers"]
pkgdesc = "Small utilities that use the proc file-system"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/psmisc/psmisc"
source = f"$(SOURCEFORGE_SITE)/psmisc/psmisc-{pkgver}.tar.xz"
sha256 = "58c55d9c1402474065adae669511c191de374b0871eec781239ab400b907c327"
hardening = ["vis", "cfi"]
# dejagnu
options = ["!check"]
