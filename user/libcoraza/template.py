pkgname = "libcoraza"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["go", "pkgconf", "automake", "slibtool"]
checkdepends = ["bash"]
pkgdesc = "Command-line fuzzy finder"
license = "Apache-2.0"
url = "https://github.com/corazawaf/libcoraza"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f887fcb2d825441c47cb4cc5b3a5edfa66baf19e1aba8d76c2e4e8abaee022d2"


def post_extract(self):
    # the reconf fails because this file is "required"
    self.cp("CHANGELOG.md", "ChangeLog")


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_build(self):
    # build tests
    self.make.invoke("tests/simple_get")
    self.cp("tests/simple_get.out", f"{self.make_dir}/tests")


def check(self):
    # fails with segfault due to:
    # https://github.com/golang/go/issues/13492
    # and unmerged PR to address it, which explains the incompatibility:
    # https://github.com/golang/go/pull/75048
    # I think that means it won't work at all on Chimera for now
    self.do(
        self.chroot_srcdir / "tests" / "check_result.sh",
        "simple_get",
        wrksrc=f"{self.make_dir}/tests",
    )
