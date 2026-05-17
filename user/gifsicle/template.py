pkgname = "gifsicle"
pkgver = "1.96"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-gifview",
]
hostmakedepends = ["automake"]
pkgdesc = "GIF manipulation and optimization tool"
license = "GPL-2.0-only"
url = "http://www.lcdf.org/gifsicle"
source = (
    f"https://github.com/kohler/gifsicle/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "1104b338745f466bdb6b739b152c42a5dfe2fb50a4c21e3bcd78446766f007ea"
