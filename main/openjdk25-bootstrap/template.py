pkgname = "openjdk25-bootstrap"
pkgver = "25.0.2_p10"
pkgrel = 0
# satisfy revdeps
makedepends = [
    "alsa-lib-devel",
    "freetype-devel",
    "giflib-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxt-devel",
    "libxtst-devel",
]
pkgdesc = "Bootstrap binaries of OpenJDK 25"
license = "GPL-2.0-only WITH Classpath-exception-2.0"
url = "https://openjdk.org"
#  source = f"https://repo.chimera-linux.org/distfiles/openjdk-bootstrap-{pkgver}-{self.profile().arch}.tar.zst"
# find downloads at: https://jdk.java.net/archive/
source = "https://download.java.net/java/GA/jdk25.0.2/b1e0dfa218384cb9959bdcb897162d4e/10/GPL/openjdk-25.0.2_linux-x64_bin.tar.gz"
options = ["!strip"]

match self.profile().arch:
    # case "aarch64":
    #     sha256 = (
    #         "65e8520f8a2b0055335b2a75f3dd10a5242b846529fc36a1f16806b1639f7515"
    #     )
    # case "ppc64":
    #     sha256 = (
    #         "e57ca2ee5a8f97c4571553253c6e52d4944d69cb5c718a5e64989359b7415392"
    #     )
    # case "ppc64le":
    #     sha256 = (
    #         "83a098ec36fb0be90ff671739942a86d0675f63482a399ad88725b92beec69e7"
    #     )
    case "x86_64":
        sha256 = (
            "555ce0821e4fe175ea50d54518cd6fbece9663c1998de529bc6ce429534457df"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    self.install_dir("usr/lib/jvm/java-25-openjdk")
    for f in self.cwd.iterdir():
        self.install_files(f, "usr/lib/jvm/java-25-openjdk")
