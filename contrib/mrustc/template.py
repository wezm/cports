pkgname = "mrustc"
pkgver = "1.54.0"
pkgrel = 0
_gitrev = "c70b86e138018b0e144dd179a5bd6c6e0972b350"
_outdir = f"output-{pkgver}"
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["-f", "minicargo.mk", "V="]
# make_build_args = ["-f", "minicargo.mk", f"{_outdir}/libstd.rlib", "V="]
make_check_target = f"{_outdir}/rust/test_run-pass_hello"
make_check_args = ["-f", "minicargo.mk", "V="]
make_use_env = True # FIXME: pass CXXFLAGS as CXXFLAGS_EXTRA
# TODO: Can we patch out bash
# TODO: Remove curl if its no longer used
# TODO: What bash script calls git -- probably doesn't matter since it's not in a git repo
# TODO: Can we use the system llvm, I guess not since it's tied to the Rust version
hostmakedepends = ["pkgconf", "gmake", "bash", "curl", "cmake", "pkgconf", "python", "git", "llvm"]
makedepends = ["zlib-devel"]
pkgdesc = "Bootstrap Rust compiler implemented in C++"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/thepowersgang/mrustc"
source = [
    f"{url}/archive/{_gitrev}.tar.gz",
    f"https://static.rust-lang.org/dist/rustc-{pkgver}-src.tar.gz"
]
source_paths = [
    ".",
    f"rustc-{pkgver}-src",
]
sha256 = [
  "4e259ec117bc5b387fd3a9702c889f46940787e135ad00ee0721fa35352c16b4",
  "ac8511633e9b5a65ad030a1a2e5bdaa841fdfe3132f2baaa52cc04e71c6c6976",
]
env = {
    "RUSTC_VERSION": pkgver, 
    "MRUSTC_TARGET_VER": "1.54",  # FIXME: derive from pkgver
    "RUSTC_TARGET": "x86_64-chimera-linux-musl",
    "LLVM_CONFIG": "/usr/bin/llvm-config",
}
# options = ["!parallel"]

# def do_prepare(self):
#     self.make.invoke(["RUSTCSRC"])

def pre_build(self):
    # FIXME: Maybe it would be better to just vendor the patch
    self.do("sh", "-c", f"patch -p0 < ../rustc-{pkgver}-src.patch", wrksrc = f"rustc-{pkgver}-src")
    self.do("touch", f"rustc-{pkgver}-src/dl-version")
    self.do("touch", f"rustc-{pkgver}-src.tar.gz") # stop it trying to download

# TODO: Silence this warning: -Wunqualified-std-cast-call
# TODO: Can we stop it stripping/objcopy


# pkgname = "libedit"
# pkgver = "20230530"
# pkgrel = 0
# _gitrev = "bcf25b69b1a52b9b9b33c17e742f429983e30b9d"
# build_style = "makefile"
# make_cmd = "gmake"
# hostmakedepends = ["pkgconf", "gmake"]
# makedepends = ["ncurses-devel"]
# pkgdesc = "Port of the NetBSD command line editing library"
# maintainer = "q66 <q66@chimera-linux.org>"
# license = "BSD-3-Clause"
# url = "https://github.com/chimera-linux/libedit-chimera"
# source = f"{url}/archive/{_gitrev}.tar.gz"
# sha256 = "c27333d42900ce01b970c8038764b80ea65838d1a08b301e86e8ea0647b3562e"
