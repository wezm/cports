pkgname = "syft"
pkgver = "1.22.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver}",
    "./cmd/syft",
]
hostmakedepends = ["go"]
pkgdesc = "SBOM generator CLI for container images, filesystems and binaries"
license = "Apache-2.0"
url = "https://github.com/anchore/syft"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "40f0780a72245e77c72c7ab196c7a55ddba16430e9b4a4e48cf4002b46ca4283"
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
