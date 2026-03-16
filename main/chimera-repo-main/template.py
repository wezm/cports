pkgname = "chimera-repo-main"
pkgver = "0.3"
pkgrel = 0
archs = [
    "aarch64",
    "loongarch64",
    "ppc",
    "ppc64",
    "ppc64le",
    "riscv64",
    "x86_64",
]
build_style = "meta"
depends = ["apk-tools", "!base-cbuild"]
pkgdesc = "Chimera base repository"
license = "custom:meta"
url = "https://chimera-linux.org"


def install(self):
    # TODO: Get our own keys for this
    #  self.install_file(
    #      *self.find(
    #          self.files_path, f"{self.profile().arch}@chimera-linux.org-*.pub"
    #      ),
    #      "usr/lib/apk/keys",
    #  )
    self.install_file(
        self.files_path / "wes@wezm.net-65ab175a.rsa.pub",
        "usr/lib/apk/keys",
    )
    self.install_file(
        self.files_path / "01-repo-main.list", "usr/lib/apk/repositories.d"
    )
    self.install_file(
        self.files_path / "02-repo-main-debug.list",
        "usr/lib/apk/repositories.d",
    )


@subpackage("chimera-repo-main-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return ["usr/lib/apk/repositories.d/*-debug.list"]
