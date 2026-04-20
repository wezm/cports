pkgname = "akonadi-calendar-tools"
pkgver = "26.04.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-devel",
    "calendarsupport-devel",
    "kcalendarcore-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Console utilities for Akonadi calendars"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/pim/akonadi-calendar-tools"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-calendar-tools-{pkgver}.tar.xz"
sha256 = "c8e0bd48ca7f2f1d30bd5ee10e850a4648fc733a7de45d4a9242fb852475ad30"
