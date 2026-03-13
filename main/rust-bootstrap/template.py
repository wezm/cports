pkgname = "rust-bootstrap"
pkgver = "1.93.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust", "llvm-libgcc-devel"]
pkgdesc = "Rust programming language bootstrap toolchain"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://static.rust-lang.org/dist"
_triplet = self.profile().triplet
source = [
    f"{_urlb}/rustc-{pkgver}-{_triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{_triplet}.tar.xz",
]
# !splitstatic and !lto to avoid the static lint
options = ["!strip", "!splitstatic", "!lto"]

match self.profile().arch:
    # case "aarch64":
    #     sha256 = [
    #         "f525efe0f9fe418d976b1447ec5ff6c075f7d32756f8b7ede258e4384ecbada3",
    #         "6cc88202832f6d003c191a45ede4196ef43cec05d763cec5cf69f33694e75a93",
    #     ]
    # case "loongarch64":
    #     sha256 = [
    #         "aa22a5d3dee1c2a0194cb3a04e32f6b0c3e5bbaa730e9f82dff716e7b2c836dd",
    #         "bd6cd31f41f2ba03d2458ee95a0501f9cbef4a5e3aabac177cf0f2431c18522f",
    #     ]
    # case "ppc64le":
    #     sha256 = [
    #         "dfb4007a93577f52d8aaba559a4eb1d5a354d5c3d7c694dee6f30b0d6dae8c19",
    #         "7a6a4bfcf425cfc3116260235545e1fe6c037a8fb6a3dc9c320f071c0595eb69",
    #     ]
    # case "ppc64":
    #     sha256 = [
    #         "61bee27932b6bad31edaa9806353d5bb1b1b88dd95d97986f4f6638963d4191e",
    #         "0d58ef934ea8a4555cdd2d3f20781d7f3c71279b71b08ee0bcc350954858919d",
    #     ]
    # case "ppc":
    #     sha256 = [
    #         "58124a1a2ffd24b957132fd6a2e635aa4a0be010a21bf2ccd5516b1abc6ce012",
    #         "72670f1e5849582c5cecb26613ef6ee7fc5c283ea1c5005244f2cea284b5fe96",
    #     ]
    # case "riscv64":
    #     sha256 = [
    #         "aaf905bf3c81c37e428ca2f66935d0d49f22d418159b20159bbccd1fac71ccff",
    #         "a358010bbf48a1caf67da82e0ddc8135427e98c10400f10292f090ec1921874b",
    #     ]
    case "x86_64":
        sha256 = [
            "00c6e6740ea6a795e33568cd7514855d58408a1180cd820284a7bbf7c46af715",
            "a849a418d0f27e69573e41763c395e924a0b98c16fcdc55599c1c79c27c1c777",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    for d in self.cwd.iterdir():
        self.do(
            "/bin/sh",
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    self.uninstall(f"usr/lib/rustlib/{_triplet}/bin")
    # whatever
    self.uninstall("usr/etc")
    # licenses
    self.install_license(f"rustc-{pkgver}-{_triplet}/LICENSE-MIT")
