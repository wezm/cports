pkgname = "cosmic-wallpapers"
pkgver = "1.0.15"
pkgrel = 0
pkgdesc = "Wallpapers for the COSMIC desktop environment"
license = "GPL-3.0-only"
url = "https://github.com/pop-os/cosmic-wallpapers"
source = f"{url}/archive/refs/tags/epoch-{pkgver}.tar.gz"
sha256 = "9bd3f7bfa426eddc8ae8bcab0eb81b77821bcc02350befa67ea400bb9ef8400c"


def install(self):
    prefix = self.chroot_destdir / "usr"
    self.do("make", "install", f"prefix={prefix}")
