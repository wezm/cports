pkgname = "perl-image-exiftool"
pkgver = "13.50"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for editing exif metadata"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://exiftool.org"
source = f"$(SOURCEFORGE_SITE)/exiftool/Image-ExifTool-{pkgver}.tar.gz"
sha256 = "27e2d66eb21568cc0d59520f89afcaaa50735e1ad9fa4b36d0a4ccf916c70d31"


@subpackage("perl-image-exiftool-progs")
def _(self):
    self.depends += [self.parent]
    self.renames = ["exiftool"]

    return self.default_progs()
