pkgname = "tailscale"
pkgver = "1.96.5"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X tailscale.com/version.longStamp={pkgver}"
    + f" -X tailscale.com/version.shortStamp={pkgver}",
    "./cmd/tailscale",
    "./cmd/tailscaled",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
depends = ["iptables", "ca-certificates"]
pkgdesc = "Mesh VPN daemon based on WireGuard"
license = "BSD-3-Clause"
url = "https://github.com/tailscale/tailscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "67fd4cb847f51d54feab8efeba915883304be276ce1c58a44a047bd62fd761db"
# check: needs network access
# cross: completions with host bin
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"tailscale.{shell}", "w") as outf:
            self.do(
                f"{self.make_dir}/tailscale",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/tailscaled")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_file("^/envfile", "usr/share/tailscale")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"tailscale.{shell}", shell)
