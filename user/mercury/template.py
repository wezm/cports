pkgname = "mercury"
pkgver = "2022.02.26"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-csharp-grade",
    "--disable-java-grade",
    # "--enable-libgrades=asm_fast.gc,asm_fast.gc.debug.stseg,hlc.gc,hlc.gc.memprof,hlc.gc.prof,hlc.par.gc,asm_fast.gc.profdeep.stseg",
    "--enable-libgrades=hlc.gc,hlc.gc.memprof,hlc.gc.prof,hlc.par.gc",
]
make_cmd = "gmake"
make_dir = "."
# make_build_args = ["SHELL=/bin/bash"]
# make_install_args = ["SHELL=/bin/bash"]
hostmakedepends = ["gmake", "pkgconf", "flex", "bison"]
pkgdesc = "Mercury compiler"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-2.0-only"
url = "http://www.mercurylang.org"
source = f"https://github.com/Mercury-Language/mercury-srcdist/archive/rotd-{pkgver.replace('.', '-')}.tar.gz"
# source = f"http://dl.mercurylang.org/rotd/mercury-srcdist-rotd-${pkgver.replace('.', '-')}.tar.xz"
sha256 = "c9f994fcfe55af3d8dddb72484bf5635e8efc1dbed45e9c3e70bf1dbafe0acba"
# no check target
options = ["!check", "!lto", "!splitstatic"]

configure_gen = []

def post_install(self):
    for f in (self.destdir / "usr/bin").glob("*.bat"):
        f.unlink()
    
