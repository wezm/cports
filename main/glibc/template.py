_trip = "x86_64-pc-linux-gnu"
pkgname = f"glibc"
pkgver = "2.42"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    # TODO: cross
    #  f"--host={_trip}"
    #  "--build=$(../scripts/config.guess)"
    # "--with-headers=/usr/include",
    #  "--with-bugurl=https://bugs.archlinux.org/",
    #  "--sbindir=/usr/bin",
    #  "--libdir=/usr/lib",
    #  "--mandir=/usr/share/man",
    #  "--infodir=/usr/share/info",
    "--enable-bind-now",
    "--enable-cet",
    "--enable-fortify-source",
    "--enable-kernel=4.4",  # LFS uses 4.14, drawbacks to that?
    #  "--enable-multi-arch",
    "--enable-stack-protector=strong",
    "--disable-profile",
    "--disable-werror",
    "--with-gd=no",
]
# These auxiliary programs are missing or incompatible versions: msgfmt makeinfo
hostmakedepends = [
    "binutils",
    "bison",
    "gawk",
    "gcc",
    "gmake",
    "gsed",
    "python",
    "texinfo",
]
makedepends = ["linux-headers"]
depends = []
pkgdesc = "GNU libc"
# maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libc"
source = f"$(GNU_SITE)/glibc/glibc-{pkgver}.tar.xz"
# [azanella/clang] 6bc4b13
# source = "https://files.wezm.net/chimera/glibc.tar.xz"
sha256 = "d1775e32e4628e64ef930f435b67bb63af7599acb6be2b335b9f19f16509f17f"
tools = {
    "CC": "gcc",
    "CXX": "g++",
    "CPP": "cpp",
    "AS": "as",
    "LD": "ld.bfd",
    "OBJDUMP": "objdump",  # TODO: gobjdump
}
# resistance is futile
options = ["bootstrap", "!check", "!lto"]  # TODO: check

# work around:
# objdump -f /builddir/glibc-2.42/build/format.lds.so | sed -n 's/.*file format \(.*\)/OUTPUT_FORMAT(\1)/;T;p' > /builddir/glibc-2.42/build/format.lds
# sed: 1: "s/.*file format \(.*\)/ ...": invalid command code T
exec_wrappers = [("/usr/bin/gsed", "sed")]

configure_gen = []

#  if self.stage > 0:
#      configure_args += ["--enable-systemtap"]

if self.stage > 0:
    # have base-files extract first in normal installations
    #
    # don't do this for stage 0 though, because otherwise base-files will
    # get installed as a makedepend and subsequently removed as an autodep,
    # which will nuke the base symlinks handled by initial initdb, as the
    # stage0 bldroot is not a complete chroot and relies on the external
    # state we give it during first setup
    #
    # but this only really matters for "real" systems, so in stage 0 we can
    # just avoid the dependency and work around the whole issue
    #
    depends += ["base-files"]
    # This ensures that /etc/hosts is present, whicih is necessary for some
    # tests to pass in stage 2.


def pre_configure(self):
    build_dir = self.cwd / self.make_dir
    build_dir.mkdir()
    with open(build_dir / "configparms", "w") as cf:
        cf.write(
            """
slibdir=/usr/lib
libdir=/usr/lib
rtlddir=/usr/lib
sbindir=/usr/bin
rootsbindir=/usr/bin
"""
        )


def post_install(self):
    # hardlink detected (usr/libexec/getconf/POSIX_V7_LP64_OFF64, previously usr/libexec/getconf/XBS5_LP64_OFF64)
    # hardlink detected (usr/libexec/getconf/POSIX_V6_LP64_OFF64, previously usr/libexec/getconf/XBS5_LP64_OFF64)
    # hardlink detected (usr/bin/getconf, previously usr/libexec/getconf/XBS5_LP64_OFF64)

    # fix up hardlinks
    self.uninstall("usr/libexec/getconf/POSIX_V6_LP64_OFF64")
    self.install_link(
        "usr/libexec/getconf/POSIX_V6_LP64_OFF64", "XBS5_LP64_OFF64"
    )

    self.uninstall("usr/libexec/getconf/POSIX_V7_LP64_OFF64")
    self.install_link(
        "usr/libexec/getconf/POSIX_V7_LP64_OFF64", "XBS5_LP64_OFF64"
    )

    self.uninstall("usr/bin/getconf")
    self.install_link("usr/bin/getconf", "../libexec/getconf/XBS5_LP64_OFF64")

    #  self.install_link("lib", "usr/lib64")

    # Violates `/var` lint
    # TODO: Replace functionality with?
    # https://salsa.debian.org/debian/nss-updatedb

    # Debian splits this out as libnss-db:

    # dpkg -L libnss-db
    #  /.
    #  /etc
    #  /etc/default
    #  /etc/default/libnss-db
    #  /usr
    #  /usr/bin
    #  /usr/bin/makedb
    #  /usr/lib
    #  /usr/lib/x86_64-linux-gnu
    #  /usr/lib/x86_64-linux-gnu/libnss_db-2.2.3.so
    #  /usr/share
    #  /usr/share/doc
    #  /usr/share/doc/libnss-db
    #  /usr/share/doc/libnss-db/NEWS.gz
    #  /usr/share/doc/libnss-db/README
    #  /usr/share/doc/libnss-db/changelog.Debian.gz
    #  /usr/share/doc/libnss-db/copyright
    #  /usr/share/man
    #  /usr/share/man/man1
    #  /usr/share/man/man1/makedb.1.gz
    #  /var
    #  /var/lib
    #  /var/lib/misc
    #  /var/lib/misc/Makefile
    #  /usr/lib/x86_64-linux-gnu/libnss_db.so.2

    # Note they also patch it so that it gets put in /var/lib/misc/Makefile
    # LFS has this patch:
    # wcurl https://www.linuxfromscratch.org/patches/lfs/development/glibc-2.42-fhs-1.patch -o main/glibc/patches/fhs.patch

    self.uninstall("var/db/Makefile")


@subpackage("glibc-devel")
def _(self):
    self.options = ["!splitstatic"]
    self.depends += ["linux-headers"]
    return self.default_devel()
