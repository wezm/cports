pkgname = "cosmic-greeter"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
# skip systemd feature
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
    "dav1d-devel",
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
sha256 = "d8d4135d926c0f2673dbb8ddb6120a7dc5f992811798ca193372db904f385f76"
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
        self.files_path / "cosmic-greeter.pam",
        "usr/lib/pam.d",
        name="cosmic-greeter",
    )

    self.install_service(self.files_path / "cosmic-greeter-daemon")
    self.install_service(self.files_path / "cosmic-greeter")

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
