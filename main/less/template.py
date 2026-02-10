pkgname = "less"
pkgver = "691"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
checkdepends = ["perl"]
pkgdesc = "Pager program similar to more(1)"
license = "custom:less OR GPL-3.0-or-later"
url = "https://www.greenwoodsoftware.com/less"
source = f"https://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "88b480eda1bb4f92009f7968b23189eaf1329211f5a3515869e133d286154d25"
hardening = ["vis", "cfi"]
# FIXME
# DIFF utf8-2.txt on cmd #20 (. a)
# FAIL: utf8-2.txt (20 steps)
# ERR  status 256 from /builddir/less-691/lesstest/lesstest  -e  -s '/builddir/less-691/lesstest/lt_screen' -t '/builddir/less-691/lesstest/lt/utf8-2.txt.lt' '/builddir/less-691/build/less'
# "hdr-unicode" may be a binary file.  See it anyway? ;0;4452R^C
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("^/lesspipe.sh", "usr/bin", mode=0o755)
    self.install_file("^/zless.sh", "usr/bin", mode=0o755, name="zless")
    self.install_link("usr/bin/more", "less")
    self.install_link("usr/share/man/man1/more.1", "less.1")
    self.install_link("usr/bin/bzless", "zless")
    self.install_link("usr/bin/xzless", "zless")
    self.install_link("usr/bin/lzless", "zless")
    self.install_link("usr/bin/zstdless", "zless")
