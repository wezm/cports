pkgname = "linkedlist"
# pkgver = "2.0.0_git20241108"
# until this is fixed: https://github.com/pyinfra-dev/pyinfra/pull/1233
pkgver = "2.0.17"
pkgrel = 0
_gitrev = "493751b"
_token = self.get_data("forge_token")
build_style = "cargo"
make_build_args = ["--bin", "linkedlistd"]
make_install_args = [*make_build_args]
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
sha256 = "3c4082479769e838754a73e0f1b9551e25c5e6953984cc6d066d75e457ec09cb"

def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "linkedlist")
