_trip = "x86_64-pc-linux-gnu"
pkgname = f"gcc-bootstrap"
pkgver = "13.2.0"
_mpfr_ver = "4.2.0"
_gmp_ver = "6.3.0"
_mpc_ver = "1.3.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    f"--target={_trip}",
    # TODO: cross
    #  f"--host={_trip}"
    #  "--build=$(../scripts/config.guess)"
    "--with-glibc-version=2.38",
    f"--with-sysroot=/usr/{_trip}",
    "--disable-bootstrap", # because https://stackoverflow.com/questions/46487529/crosscompiling-gcc-link-tests-are-not-allowed-after-gcc-no-executables-when-che
    "--with-newlib",
    "--without-headers",
    "--enable-default-pie",
    "--enable-default-ssp",
    "--disable-nls",
    "--disable-shared",
    #  "--enable-shared",
    "--disable-multilib",
    "--disable-threads",
    "--disable-libatomic",
    "--disable-libgomp",
    "--disable-libquadmath",
    "--disable-libssp",
    "--disable-libvtv",
    "--disable-libstdcxx",
    "--enable-languages=c,c++",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "binutils"] # FIXME: Is binutils needed?
makedepends = ["glibc-devel"]
pkgdesc = "GNU Compiler Collection"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libc"
source = [# source_paths
    f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz",
    f"$(GNU_SITE)/mpfr/mpfr-{_mpfr_ver}.tar.xz",
    f"$(GNU_SITE)/gmp/gmp-{_gmp_ver}.tar.xz",
    f"$(GNU_SITE)/mpc/mpc-{_mpc_ver}.tar.gz",
]
source_paths = [
    ".",
    "mpfr",
    "gmp",
    "mpc"
]

sha256 = [
    "e275e76442a6067341a27f04c5c6b83d8613144004c0413528863dc6b5c743da",
    "06a378df13501248c1b2db5aa977a2c8126ae849a9d9b7be2546fb4a9c26d993",
    "a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898",
    "ab642492f5cf882b74aa0cb730cd410a81edcdbec895183ce930e706c1c759b8",

]
# resistance is futile
options = ["bootstrap", "!check", "!lto"] # TODO: check

if self.stage == 0:
    options += ["!scanrundeps"]

hardening = ["!pie"]

# FIXME
#  nopie_files = ["usr/bin/x86_64-pc-linux-gnu-gcc-*", "usr/bin/gcov*", "usr/libexec/gcc/x86_64-pc-linux-gnu/13.2.0/*"]

configure_gen = []


#  def pre_configure(self):
#      build_dir = (self.cwd / self.make_dir)
#      build_dir.mkdir()
#      with open(build_dir / "configparms", "w") as cf:
#          cf.write(
#              f"""
#  slibdir=/usr/lib
#  rtlddir=/usr/lib
#  sbindir=/usr/bin
#  rootsbindir=/usr/bin
#  """
#          )

#  def post_configure(self):
#      1 / 0

def post_install(self):
    for f in ["c++", "gcc-nm", "g++", "gcc", "gcc-ranlib", "gcc-ar"]:
        self.rm(self.destdir / f"usr/bin/{f}")
        self.install_link(f"../{_trip}-{f}", f"usr/bin/{f}")

    self.rm(self.destdir / "usr/bin/x86_64-pc-linux-gnu-c++")
    self.install_link("x86_64-pc-linux-gnu-g++", "usr/bin/x86_64-pc-linux-gnu-c++")

    self.rm(self.destdir / "usr/bin/x86_64-pc-linux-gnu-gcc")
    self.install_link(f"x86_64-pc-linux-gnu-gcc-{pkgver}", "usr/bin/x86_64-pc-linux-gnu-gcc")



#  @subpackage("glibc-devel")
#  def _devel(self):
#      return self.default_devel()

