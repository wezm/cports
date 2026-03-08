pkgname = "pax-utils"
pkgver = "1.3.10"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlddtree_implementation=python",
    "-Duse_libcap=enabled",
    "-Duse_fuzzing=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "libcap-devel",
    "linux-headers",
]
checkdepends = [
    "bash",
    "python-pyelftools",
]
pkgdesc = "ELF related utils for ELF binaries"
license = "GPL-2.0-only"
url = "https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities"
source = f"https://dev.gentoo.org/~floppym/dist/pax-utils-{pkgver}.tar.xz"
sha256 = "2d308a923a846a0a816bf9c9fd05b5f38371e9dcfafbf976159a76f3e8e7d317"
hardening = ["vis", "cfi"]
# see below
options = []


match self.profile().arch:
    case "ppc64le" | "ppc64":
        # FIXME lddtree/scanelf fail
        options += ["!check"]


@subpackage("pax-utils-lddtree")
def _(self):
    self.depends += ["python-pyelftools"]
    self.install_if = [self.parent, "python"]
    self.provides = [self.with_pkgver("lddtree")]
    self.pkgdesc = "Print ELF dependency trees"
    return ["usr/bin/lddtree"]


@subpackage("pax-utils-symtree")
def _(self):
    self.depends += [self.parent, "bash"]
    self.install_if = [self.parent, "bash"]
    self.provides = [self.with_pkgver("symtree")]
    self.pkgdesc = "Display libraries that satisfy undefined symbols"
    return ["usr/bin/symtree"]
