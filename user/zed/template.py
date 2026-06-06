pkgname = "zed"
pkgver = "1.18.0"
pkgrel = 0
# wasmtime
archs = ["aarch64", "x86_64"]
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--package",
    "zed",
    "--package",
    "cli",
    "--package",
    "remote_server",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "alsa-lib-devel",
    "curl-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libxkbcommon-devel",
    "rust-bindgen",
    "rust-std",
    "sqlite-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# otherwise downloads a non-working one
depends = ["nodejs"]
pkgdesc = "Graphical text editor"
license = "GPL-3.0-or-later AND Apache-2.0"
url = "https://zed.dev"
source = f"https://github.com/zed-industries/zed/archive/v{pkgver}.tar.gz"
sha256 = "939dde198f36d917e372e7a4e10b07ed7d1ae7d720652ca40f9cefc544c35bdc"
# workaround code that fails with default gc-sections with lld
# https://github.com/zed-industries/zed/issues/15902
tool_flags = {"RUSTFLAGS": ["-Clink-arg=-Wl,-lc,-z,nostart-stop-gc"]}
env = {
    "RELEASE_VERSION": pkgver,
    "ZED_UPDATE_EXPLANATION": "Managed by system package manager",
    "ZED_RELEASE_CHANNEL": "stable",
}
# no, aws-lc-sys build fails
options = ["!check", "!cross"]


def post_prepare(self):
    from cbuild.util import cargo, patch

    # done separately because we need to patch lockfile before vendoring :/
    patch.patch(self, [self.files_path / "aws-lc-sys.patch"])

    cargo.clear_vendor_checksums(self, "aws-lc-sys-0.42.0")


def init_build(self):
    with open(self.cwd / "crates/zed/RELEASE_CHANNEL", "w") as cf:
        cf.write(self.env["ZED_RELEASE_CHANNEL"])


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/zed",
        "usr/lib/zed",
        name="zed-editor",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli",
        name="z",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/remote_server",
        name="zed-server",
    )
    self.install_file(
        "crates/zed/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="dev.zed.Zed.png",
    )
    self.install_file(
        "crates/zed/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="dev.zed.Zed.png",
    )
    self.install_file(
        "crates/zed/resources/zed.desktop.in",
        "usr/share/applications",
        name="dev.zed.Zed.desktop",
    )
    self.install_license("LICENSE-GPL")


@subpackage("zed-server")
def _(self):
    self.subdesc = "Zed remote server"

    return ["usr/bin/zed-server"]
