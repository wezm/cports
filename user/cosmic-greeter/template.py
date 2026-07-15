pkgname = "cosmic-greeter"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    "--all",
    "--no-default-features",
    "--features",
    "logind,networkmanager,upower",
]
make_build_env = {
    # dummy values to stop it trying to run git
    "VERGEN_GIT_COMMIT_DATE": "2026-03-27",
    "VERGEN_GIT_SHA": "0000000000000000000000000000000000000000",
}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "rust-std",
    "udev-devel",
    "zstd-devel",
]
depends = ["clang-libs", "greetd", "cosmic-comp"]
pkgdesc = "COSMIC greeter for greetd"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-greeter"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "ec9921d3c2089df604d3851161d4ffb30c7630120801b86747d562d4e031cf09"
# no tests
options = ["!check", "etcfiles"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-greeter")
    self.install_bin(
        f"target/{self.profile().triplet}/release/cosmic-greeter-daemon"
    )
    self.install_bin("cosmic-greeter-start.sh", name="cosmic-greeter-start")

    self.install_file("cosmic-greeter.toml", "etc/greetd")
    self.install_file(
        "dbus/com.system76.CosmicGreeter.conf", "usr/share/dbus-1/system.d"
    )
    self.install_file(
        "^/cosmic-greeter.pam", "usr/lib/pam.d", name="cosmic-greeter"
    )

    self.install_service("^/cosmic-greeter-daemon")
    self.install_service("^/cosmic-greeter")

    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
