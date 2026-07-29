pkgname = "fondu"
pkgver = "060102"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Macintosh font conversion tools"
license = "BSD-3-Clause"
url = "https://fondu.sourceforge.net"
source = f"{url}/fondu_src-{pkgver}.tgz"
sha256 = "22bb535d670ebc1766b602d804bebe7e84f907c219734e6a955fcbd414ce5794"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
