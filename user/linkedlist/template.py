pkgname = "linkedlist"
# pkgver = "2.0.0_git20241108"
# until this is fixed: https://github.com/pyinfra-dev/pyinfra/pull/1233
pkgver = "2.0.16"
pkgrel = 0
_gitrev = "8be02f9"
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
sha256 = "89700a98232adc873835ec7dac2cb60952d16feca8f7e991281e95e8419eb618"

def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "linkedlist")
