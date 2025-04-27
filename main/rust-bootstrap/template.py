pkgname = "rust-bootstrap"
pkgver = "1.86.0"
pkgrel = 1
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
if self.profile().arch == "x86" or self.profile().arch == "x86_64":
    _urlb = "https://files.wezm.net/chimera"
else:
    _urlb = "https://repo.chimera-linux.org/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz",
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "3943f15a5f435c98c0ab0015d50461768d340bba0c4dba6aaefcfe5dea4f7c00",
            "f42f20901f313c240643937261c84759c6a674452a8ed0a2c721813964de2cbb",
        ]
    case "loongarch64":
        sha256 = [
            "07e77b9e1fd35714ff0769fd5ffc526b7409087fdfe355057cc26ef78823c858",
            "5351bddb2991e8717201307c3dd4b435e66143d718e195ab59c447c989b28cce",
        ]
    case "ppc64le":
        sha256 = [
            "53cd894d374244bf1ddc286e7f794838db8042f0638fe1f3b91eb8d6f7c5dff9",
            "a01eeb3a0ea798a0deccbb73bbf49718553a317c5b8067957b4f940d816a6303",
        ]
    case "ppc64":
        sha256 = [
            "5ce43a788db90355f0aff8e0dbb277c6d3f84866bc385195ae497c235d0cae60",
            "c24df86a4cc03e8adef13fe4fe2b481d36cbb2c81e699c2e1a4ca1af8cf4d87a",
        ]
    case "ppc":
        sha256 = [
            "9cec79a7cb4eed52f4f91220beded044bd0ff056385946d610016b33c01913ed",
            "5f1383e08499f7e65530037f363c3f9eb2bb9a7cc17089c9bb1ea78d902f6a35",
        ]
    case "riscv64":
        sha256 = [
            "8d590e01be55a77111b2f09402f252194acc58d13f42dc951e1756d47dfc5a24",
            "b435f433b116834cf21bd8ba4d263542f2007a0542feb4f7b3dd7792321a2ed2",
        ]
    case "x86":
        sha256 = [
            "dc4caea35e2e920921302ab558b22cfb873a115822574c3b90fe8bf7320a5f2a",
            "4503e0075ba2554d6848b73cc74b3b14282a1b0ebfe9f7d8383b6d8a69aecebf",
        ]
    case "x86_64":
        sha256 = [
            "3516b5ab59bae74f2819d5dda1d2676179cea542ddbfe94735f7bd345a1e3a5d",
            "ba225518a9020fdafebf413bb35951c4afe84450f9d15cbe5107b4be94fe313e",
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
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
