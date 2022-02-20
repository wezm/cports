pkgname = "awesome"
pkgver = "4.3"
pkgrel = 0
build_style = "cmake"
#configure_args = ["-DLUA_EXECUTABLE=lua5.1"]
hostmakedepends = ["cmake", "lua5.1", "lua5.1-lgi", "ninja", "pkgconf"] # LGI does not work with Lua5.4 yet
# TODO: Add asciidoctor for documentation
# TODO: review deps in awesomeConfig.cmake (glib?)
makedepends = [
    "libxcb-devel", "pango-devel", "xcb-util-devel", "xcb-util-image-devel",
    "xcb-util-keysyms-devel", "xcb-util-wm-devel", "xcb-util-cursor-devel",
    "startup-notification-devel", "imlib2-devel", "libxdg-basedir-devel",
    "gdk-pixbuf-devel", "dbus-devel", "libxkbcommon-devel", "xcb-util-xrm-devel",
    "lua5.1-devel", "lua5.1-lgi", "imagemagick"
]
depends = ["dbus-x11", "pango", "lua5.1-lgi", "fonts-dejavu-otf"]
pkgdesc = "Awesome is a highly configurable window manager for X"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-2.0-or-later"
url = "https://awesomewm.org"
source = f"https://github.com/awesomeWM/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "78264d6f012350b371e339127aca485260bc0aa935eff578ba75ce1a00e11753"
tool_flags = { "CFLAGS": [ "-fcommon" ] } # https://wiki.gentoo.org/wiki/Gcc_10_porting_notes/fno_common

# requires graphical environment
options = ["!check"]
