pkgname = "wezm-repo-main"
pkgver = "0.3"
pkgrel = 0
archs = [
    "x86",
]
build_style = "meta"
depends = ["apk-tools", "!base-cbuild"]
pkgdesc = "Chimera base repository for x86"
license = "custom:meta"
url = "https://files.wezm.net"


def install(self):
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


@subpackage("wezm-repo-main-debug")
def _(self):
    self.subdesc = "debug packages"
    self.depends = [self.parent]

    return ["usr/lib/apk/repositories.d/*-debug.list"]
