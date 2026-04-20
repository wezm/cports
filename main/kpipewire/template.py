pkgname = "kpipewire"
pkgver = "6.6.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pipewire",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "libva-devel",
    "pipewire-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "KDE Components for Flatpak pipewire usage in Plasma"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kpipewire"
source = f"$(KDE_SITE)/plasma/{pkgver}/kpipewire-{pkgver}.tar.xz"
sha256 = "1b9ef2890be00ee96ca439770a3f7842f54ac901c6a47edd3d68aff85c1a3a8f"
hardening = ["vis"]
# only available test needs running pipewire
options = ["!check"]


@subpackage("kpipewire-devel")
def _(self):
    self.depends += ["pipewire-devel"]

    return self.default_devel()
