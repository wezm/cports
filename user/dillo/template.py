pkgname = "dillo"
pkgver = "3.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-experimental-fltk",
    "--enable-gif",
    "--enable-ipv6",
    "--enable-jpeg",
    "--enable-openssl",
    "--enable-png",
    "--enable-svg",
    "--enable-tls",
    "--enable-webp",
    "--with-ca-certs-dir=/etc/ssl/certs",
]
hostmakedepends = ["automake"]
makedepends = [
    "fltk-devel",
    "libdecor-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "libxcursor-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "openssl3-devel",
]
pkgdesc = "Small graphical web browser"
license = "GPL-3.0-or-later"
url = "https://dillo-browser.org"
source = f"{url}/release/{pkgver}/dillo-{pkgver}.tar.gz"
sha256 = "db1863261d5efbd27b090e430c88064082b891cea1edf7a14e234cca51754f60"
