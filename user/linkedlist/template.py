pkgname = "linkedlist"
# pkgver = "2.0.0_git20241108"
# until this is fixed: https://github.com/pyinfra-dev/pyinfra/pull/1233
pkgver = "2.0.9"
pkgrel = 0
_gitrev = "382af63"
_token = self.get_data("forge_token")
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "oniguruma-devel",
    "rust-std",
]
pkgdesc = "Linked List web application"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "custom:none"
url = "https://forge.wezm.net/wezm/linkedlist"
source = f"https://forge.wezm.net/api/v1/repos/wezm/linkedlist/archive/{_gitrev}.tar.gz?access_token={_token}>linkedlist-{pkgver}.tar.gz"
sha256 = "3a3112782b3487f2d46fb49407d480c56e135a35fbe99a757d97e855458bfe6b"

def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "linkedlist")
    # not needed on server
    self.uninstall("usr/bin/linkedlist")
