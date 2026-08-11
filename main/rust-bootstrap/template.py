pkgname = "rust-bootstrap"
pkgver = "1.96.1"
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
            "27925affa420e5b39227edde96d77ec6a5688631a076babbc0e4459cda3c45b4",
            "c5d399200305231d6d4b6b57509c0a57858ff635f30b0d3f11a0fb87634a457e",
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
