pkgname = "python-pillow"
pkgver = "11.3.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "Tests"
# These fail on Chimera too
# FAILED Tests/test_imagedraw.py::test_default_font_size - Failed: got different content
# FAILED Tests/test_imagefont.py::test_colr[0] - AssertionError:  average pixel value difference 38.3252 > epsilon 21.0000
# FAILED Tests/test_imagefont.py::test_colr_mask[0] - AssertionError:  average pixel value difference 32.0360 > epsilon 22.0000
# FAILED Tests/test_imagefont.py::test_default_font - Failed: got different content
make_check_args = [
    "-k",
    "not test_default_font_size "
    "and not test_colr "
    "and not test_colr_mask "
    "and not test_default_font ",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "freetype-devel",
    "lcms2-devel",
    "libavif-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "python-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
license = "MIT-CMU"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/p/pillow/pillow-{pkgver}.tar.gz"
sha256 = "3828ee7586cd0b2091b6209e5ad53e20d0649bbe87164a459d0676e035e8f523"


def post_install(self):
    self.install_license("LICENSE")
