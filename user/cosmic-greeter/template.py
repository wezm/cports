pkgname = "cosmic-greeter"
pkgver = "1.9.1"
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
    "VERGEN_GIT_SHA": "unknown",
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
depends = ["greetd", "cosmic-comp"]
pkgdesc = "COSMIC greeter for greetd"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-greeter"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "a818e9f96715a09360a083685e5eb8eab9af5fc7e58fa92c839fa801912fe32f"
# no tests
options = ["!check", "etcfiles"]


def install(self):
    self.install_bin(f"target/{self.profile.triplet}/release/cosmic-greeter")
    self.install_bin(
        f"target/{self.profile.triplet}/release/cosmic-greeter-daemon"
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
