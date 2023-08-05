pkgname = "yj"
pkgver = "5.1.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Convert between YAML, TOML, JSON, and HCL"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "Apache-2.0"
url = "https://github.com/sclevine/yj"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9a3e9895181d1cbd436a1b02ccf47579afacd181c73f341e697a8fe74f74f99d"
options = ["!debug"]
