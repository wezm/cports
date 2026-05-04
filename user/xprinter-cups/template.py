pkgname = "xprinter-cups"
pkgver = "3.13.3"
pkgrel = 0
archs = ["x86_64"]
depends = ["cups-libs"]
pkgdesc = "CUPS drivers for Xprinter printers"
license = "LicenseRef-Xprinter-Proprietary"
url = "https://www.xprintertech.com/drivers-2"
source = f"https://www.xprintertech.com/label-printer-linux-1>{pkgver}.rar"
sha256 = "ed2665af416d83b8622f3f231a7300632251ec4fa98804b675e123e052518cfa"
options = ["!distlicense", "!scanrundeps"]
# restricted = "proprietary"


def post_extract(self):
    self.do(
        "tar",
        "-xf",
        f"printer-driver-xprinter_{pkgver}_all.deb",
        "data.tar.xz",
    )
    self.do(
        "tar",
        "-xf",
        "data.tar.xz",
    )


def build(self):
    ppds = self.cwd / "usr/share/cups/model/xprinter"
    for p in ppds.iterdir():
        if p.is_file() and p.suffix == ".ppd":
            self.do("gzip", "-9n", p.relative_to(self.cwd))


def install(self):
    self.install_file(
        "opt/xprinter/printer-driver-xprinter/bin/rastertosnailep-x64",
        "usr/lib/cups/filter",
        name="rastertosnailep-xprinter",
    )
    self.install_file(
        "opt/xprinter/printer-driver-xprinter/bin/rastertosnailtspl-x64",
        "usr/lib/cups/filter",
        name="rastertosnailtspl-xprinter",
    )
    ppds = self.cwd / "usr/share/cups/model/xprinter"
    for p in ppds.iterdir():
        if p.is_file() and p.suffix == ".gz":
            self.install_file(
                p.relative_to(self.cwd), "usr/share/cups/model/xprinter"
            )
