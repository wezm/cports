pkgname = "cyme"
pkgver = "3.0.2"
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
sha256 = "1ac9956cc768d4482138455ce71fb5d62b816057dc34c181096a36be27735e0d"


def pre_prepare(self):
    # ppc64le
    self.do(
        "cargo",
        "update",
        "--package",
        "rustix",
        "--precise",
        "1.1.6",
        allow_network=True,
    )


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "udevrs-0.5.0")
