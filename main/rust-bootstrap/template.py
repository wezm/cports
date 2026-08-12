pkgname = "rust-bootstrap"
pkgver = "1.97.1"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://repo.casuarina.org/distfiles"
_triplet = self.profile().triplet
source = [
    f"{_urlb}/rustc-{pkgver}-{_triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{_triplet}.tar.xz",
]
# !splitstatic and !lto to avoid the static lint
options = ["!strip", "!splitstatic", "!lto"]

match self.profile().arch:
    case "x86_64":
        sha256 = [
            "4d5010adaa0a9299bd7b85f92f35d855c4876b05efc529eff8c3fec8307df78e",
            "f82f9719e3bfc43b52c3e7313506e852d09ef44c3a4977bbe1b57fc3964c6203",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    self.uninstall(f"usr/lib/rustlib/{trip}/bin")
    # whatever
    self.uninstall("usr/etc")
    # licenses
    self.install_license(f"rustc-{pkgver}-{trip}/LICENSE-MIT")
