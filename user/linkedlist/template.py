pkgname = "linkedlist"
# pkgver = "2.0.0_git20241108"
# until this is fixed: https://github.com/pyinfra-dev/pyinfra/pull/1233
pkgver = "2.0.19"
pkgrel = 0
_gitrev = "8792e87"
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
license = "custom:none"
url = "https://forge.wezm.net/wezm/linkedlist"
source = f"https://forge.wezm.net/api/v1/repos/wezm/linkedlist/archive/{_gitrev}.tar.gz?access_token={_token}>linkedlist-{pkgver}.tar.gz"
sha256 = "2f6beb24ba3a3c17df0f8c22580787ae91ef2291457be47a43dfd5bc1ad81a9d"

def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "linkedlist")
