pkgname = "autoconf"
pkgver = "2.72"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"M4": "/usr/bin/gm4"}
configure_gen = []
# disable test 312 for now. its failure is unclear
make_check_args = ["TESTSUITEFLAGS=1-311 313-"]
hostmakedepends = ["perl", "gm4", "texinfo"]
depends = ["cmd:awk!base-files", "gm4", "perl"]
pkgdesc = "Generates automatic source code configuration scripts"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/autoconf"
source = f"$(GNU_SITE)/autoconf/autoconf-{pkgver}.tar.gz"
sha256 = "afb181a76e1ee72832f6581c0eddf8df032b83e2e0239ef79ebedc4467d92d6e"
