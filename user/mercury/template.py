pkgname = "mercury"
pkgver = "2026.10.06"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-csharp-grade",
    "--disable-java-grade",
    # "--enable-libgrades=asm_fast.gc,asm_fast.gc.debug.stseg,hlc.gc,hlc.gc.memprof,hlc.gc.prof,hlc.par.gc,asm_fast.gc.profdeep.stseg",
    "--enable-libgrades=none.gc,none.gc.debug,none.gc.debug.stseg,hlc.gc,hlc.gc.memprof,hlc.gc.prof,hlc.par.gc",
]
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "flex", "bison", "perl"]
depends = ["gmake", "perl", "clang"]
pkgdesc = "Mercury compiler"
license = "GPL-2.0-only"
url = "http://www.mercurylang.org"
source = f"https://github.com/Mercury-Language/mercury-srcdist/archive/rotd-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "1a025c7b40a9200a56630f278e83e432e8d0b94d232b70022002fac6fa6afdfc"
# no check target
options = ["!check", "!lto", "!splitstatic"]

configure_gen = []
