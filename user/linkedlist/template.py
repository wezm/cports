pkgname = "linkedlist"
pkgver = "2.0.0_git20241108"
pkgrel = 1
_gitrev = "d057651dd7693150946ac0cf7387b338ccf1e30c"
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
sha256 = "94a02a7625f6eef97e040f8f2053860284435485a57c21916d690875394fa305"
