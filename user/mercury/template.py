pkgname = "mercury"
pkgver = "2024.02.27"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-csharp-grade",
    "--disable-java-grade",
    # "--enable-libgrades=asm_fast.gc,asm_fast.gc.debug.stseg,hlc.gc,hlc.gc.memprof,hlc.gc.prof,hlc.par.gc,asm_fast.gc.profdeep.stseg",
    "--enable-libgrades=hlc.gc,hlc.gc.memprof,hlc.gc.prof,hlc.par.gc",
]
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "flex", "bison"]
pkgdesc = "Mercury compiler"
license = "GPL-2.0-only"
url = "http://www.mercurylang.org"
source = f"https://github.com/Mercury-Language/mercury-srcdist/archive/rotd-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "45951f30686e06d016c7ce551409b4fcf406d0b01ac4ab898cfee34816db60cb"
# no check target
options = ["!check", "!lto", "!splitstatic"]

configure_gen = []
