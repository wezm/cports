# update linux-lts-zfs-bin when bumping
pkgname = "linux-lts"
pkgver = "6.6.60"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "52f9e32d5082ab94253447fd66670d0c3bb765cfcb99b0bf61d1b8eae25952ef"
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

_flavor = "generic"

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]

if self.profile().cross:
    broken = "linux-devel does not come out right"


@custom_target("generate-configs", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(self, archs, _flavor)


def init_configure(self):
    # generate scripts for packaging, just hooking to base-kernel helpers
    from cbuild.util import linux

    linux.generate_scripts(self, _flavor)


def configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-lts-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-lts-dbg")
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
