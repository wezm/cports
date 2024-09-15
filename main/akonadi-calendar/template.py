pkgname = "akonadi-calendar"
pkgver = "24.08.1"
pkgrel = 0
build_style = "cmake"
# FIXME: ?
make_check_args = ["-E", "kcalcoreserializertest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcodecs-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkleo-devel",
    "messagelib-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi calendar libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/akonadi-calendar/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-calendar-{pkgver}.tar.xz"
)
sha256 = "e06c8980a6cacbffd68c7a59ac180773dc5c1bdc322a9ebdec298a93c3c0b2f9"


@subpackage("akonadi-calendar-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "kcalendarcore-devel",
        "ki18n-devel",
        "kidentitymanagement-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()