pkgname = "syft"
pkgver = "1.11.1"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver}",
    "./cmd/syft",
]
hostmakedepends = ["go"]
pkgdesc = "SBOM generator CLI for container images, filesystems and binaries"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://github.com/anchore/syft"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2a998bc29b5a8a232056e5ea8bbdb2e17289732cbff119db50cac61c5f5d0def"
# Test suite depends on docker
# generates manpages/completions with host bins
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"syft.{shell}", "w") as outf:
            self.do("build/syft", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"syft.{shell}", shell)