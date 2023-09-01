_trip = "x86_64-pc-linux-gnu"
pkgname = f"glibc"
pkgver = "2.38"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
      "--prefix=/usr",
      # TODO: cross
      #  f"--host={_trip}"
      #  "--build=$(../scripts/config.guess)"
      "--with-headers=/usr/include",
      #  "--with-bugurl=https://bugs.archlinux.org/",
      #  "--sbindir=/usr/bin",
      #  "--libdir=/usr/lib",
      #  "--mandir=/usr/share/man",
      #  "--infodir=/usr/share/info",
      "--enable-bind-now",
      "--enable-cet",
      "--enable-fortify-source",
      "--enable-kernel=4.4", # LFS uses 4.14, drawbacks to that?
      #  "--enable-multi-arch",
      "--enable-stack-protector=strong",
      "--enable-systemtap",
      "--disable-profile",
      "--disable-werror",
      "--with-gd=no",
]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["linux-headers"]
pkgdesc = "GNU libc"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libc"
source = f"$(GNU_SITE)/glibc/glibc-{pkgver}.tar.xz"
sha256 = "fb82998998b2b29965467bc1b69d152e9c307d2cf301c9eafb4555b770ef3fd2"
# resistance is futile
options = ["bootstrap", "!check", "!lto"] # TODO: check

configure_gen = []


def pre_configure(self):
    build_dir = (self.cwd / self.make_dir)
    build_dir.mkdir()
    with open(build_dir / "configparms", "w") as cf:
        cf.write(
            f"""
slibdir=/usr/lib
rtlddir=/usr/lib
sbindir=/usr/bin
rootsbindir=/usr/bin
"""
        )

#  def post_configure(self):
#      1 / 0

def post_install(self):
    # fix up hardlinks
    self.rm(self.destdir / "usr/libexec/getconf/POSIX_V7_LP64_OFF64")
    self.install_link("POSIX_V6_LP64_OFF64", "usr/libexec/getconf/POSIX_V7_LP64_OFF64")

    self.rm(self.destdir / "usr/libexec/getconf/XBS5_LP64_OFF64")
    self.install_link("POSIX_V6_LP64_OFF64", "usr/libexec/getconf/XBS5_LP64_OFF64")

    self.rm(self.destdir / "usr/bin/getconf")
    self.install_link("..//libexec/getconf/POSIX_V6_LP64_OFF64", "usr/bin/getconf")



@subpackage("glibc-devel")
def _devel(self):
    return self.default_devel()
