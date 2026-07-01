pkgname = "cyme"
pkgver = "3.0.1"
pkgrel = 0
build_style = "cargo"
# skip integration tests that try to access /sys/bus/usb/devices
make_check_args = ["--lib", "--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "List system USB buses and devices"
license = " GPL-3.0-or-later "
url = "https://github.com/tuna-f1sh/cyme"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1d0f712d39f5d747f900829b6b9cccbfa943637b4c14d60e8a6a505162174c82"
