pkgname = "gst-plugins-base"
pkgver = "1.26.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    # stuff we don't want
    # use pulse
    "-Dalsa=disabled",
    # scuffed vorbis decoder
    "-Dtremor=disabled",
    # misc
    "-Ddoc=disabled",
    "-Dexamples=disabled",
]
make_check_args = ["--timeout-multiplier=5"]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "orc",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "cdparanoia-devel",
    "glib-devel",
    "graphene-devel",
    "gstreamer-devel",
    "iso-codes",
    "libgudev-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libsm-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "libxext-devel",
    "libxi-devel",
    "libxml2-devel",
    "libxv-devel",
    "mesa-devel",
    "opus-devel",
    "orc-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    f"gstreamer~{pkgver}",
    "orc",
]
checkdepends = ["fonts-liberation-otf"]
pkgdesc = "GStreamer base plugins"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-base/gst-plugins-base-{pkgver}.tar.xz"
sha256 = "e23189fbed2ec486690382d1055c19eeaf5aae3e95e2576fc4c884d96a90e69e"
# FIXME int
hardening = ["!int"]
# gobject-introspection
options = ["!cross"]


if self.profile().arch == "x86":
    configure_args += [
        "-Dlibvisual=disabled",
    ]
else:
    makedepends += [
        "libvisual-devel",
    ]
    depends += [
        "libvisual-plugins-meta",
    ]


@subpackage("gst-plugins-base-devel")
def _(self):
    return self.default_devel()
