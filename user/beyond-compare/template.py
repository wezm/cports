pkgname = "beyond-compare"
pkgver = "5.2.2.32209"
pkgrel = 0
archs = ["x86_64"]
hostmakedepends = ["bash"]
makedepends = ["qt6-qtbase", "qt6-qtbase-printsupport", "libstdc++"]
pkgdesc = "Compare, sync, and merge files and folders"
license = "LicenseRef-BeyondCompare-Proprietary"
url = "https://www.scootersoftware.com"
source = f"{url}/bcompare-{pkgver}.x86_64.tar.gz"
sha256 = "405941cbf588b2768d7550d38ed54c489cefef5e60d2468e5604fac10f524a40"
options = ["!distlicense"]
restricted = "proprietary"


def install(self):
    self.install_dir("usr")
    self.do("bash", "install.sh", f"--prefix={self.chroot_destdir}/usr")
    self.uninstall("usr/lib/beyondcompare/ext/*.so", glob=True)

    self.install_file("bcompare.desktop", "usr/share/applications")
    self.install_file("bcompare.xml", "usr/share/mime/packages")
    self.install_file("bcompare.png", "usr/share/icons")
    self.install_file("bcomparefull32.png", "usr/share/icons")
    self.install_file("bcomparehalf32.png", "usr/share/icons")
