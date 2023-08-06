pkgname = "waybox"
pkgver = "0.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["wayland-protocols", "wlroots-devel"]
pkgdesc = "Openbox clone for Wayland"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/wizbright/waybox"
source = f"{url}/archive/2b38536decf945dba2d66d6b185fa9646bb792df.zip"
sha256 = "ca1f60b333db297543c117c112b0c6012d8d01058a89b18978cd963623ed14e5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
