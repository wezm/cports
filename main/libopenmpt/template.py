pkgname = "libopenmpt"
pkgver = "0.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-portaudio",
    "--without-portaudiocpp",
]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "flac-devel",
    "libogg-devel",
    "libpulse-devel",
    "libsndfile-devel",
    "mpg123-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for rendering tracker music to PCM"
license = "BSD-3-Clause"
url = "https://lib.openmpt.org/libopenmpt"
source = f"https://lib.openmpt.org/files/libopenmpt/src/libopenmpt-{pkgver}+release.autotools.tar.gz"
sha256 = "627f9bf11aacae615a1f2c982c7e88cb21f11b2d6f0267946f7c82c5eae4943b"
# FIXME: several locale using tests fail
# TEST..: src/mpt/string_transcode/tests/tests_string_transcode.hpp(111): mpt::ends_with(mpt::transcode<mpt::ustring>(mpt::logical_encoding::active_locale, "abc\xC3\xA4xyz"), MPT_USTRING("xyz")):
# FAIL: UNEXPECTED EXCEPTION: basic_string
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenmpt-devel")
def _(self):
    return self.default_devel()
