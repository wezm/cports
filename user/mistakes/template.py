pkgname = "mistakes"
pkgver = "2.1.4"
pkgrel = 0
hostmakedepends = ["jpm", "git"]
makedepends = ["dinit-chimera"]
pkgdesc = "Web application for mistakes.computer"
license = "MIT"
url = "https://codeberg.org/wezm/mistakes.computer"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "ae2f8c18003ed4688efc17ec5515a58eb4ff23f8e8cb55b58c39277db17ed914"


def prepare(self):
    self.do("jpm", "-l", "load-lockfile", allow_network=True)


def build(self):
    self.do("jpm", "-l", "build")


def check(self):
    self.do("jpm", "-l", "test")


def install(self):
    self.install_bin("build/mistakes")
    self.install_file("mistakes.txt", "usr/share/mistakes")
    self.install_file("style.css", "usr/share/mistakes")
    self.install_file("favicon.png", "usr/share/mistakes")
    self.install_service("^/mistakes")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_license("LICENSE")
