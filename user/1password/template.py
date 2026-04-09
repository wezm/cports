pkgname = "1password"
pkgver = "8.12.10"
pkgrel = 0
archs = ["x86_64"]
depends = ["hicolor-icon-theme", "gtk+3", "xdg-utils", "zlib-ng-compat"]
pkgdesc = "Password manager"
license = "LicenseRef-1Password-Proprietary"
url = "https://1password.com"
source = f"https://downloads.1password.com/linux/tar/stable/x86_64/1password-{pkgver}.x64.tar.gz"
source_paths = ["1password"]
sha256 = "83d6adb7ed43439d1f5ab6ae6c991dc626b0d5ec207db66f435f2662d008aa23"
file_modes = {
    "opt/1Password/1Password-BrowserSupport": ("root", "onepassword", 0o2755),
}
options = ["!distlicense", "!scanrundeps", "!scanshlibs", "allowopt"]
restricted = "proprietary"


def install(self):
    for sz in [32, 64, 256, 512]:
        self.install_file(
            f"1password/resources/icons/hicolor/{sz}x{sz}/apps/1password.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps",
        )

    self.install_file(
        "1password/resources/1password.desktop", "usr/share/applications"
    )

    self.install_file(
        "1password/resources/custom_allowed_browsers",
        "usr/share/doc/1password/examples/",
    )

    self.install_files("1password", "opt", name="1Password")

    # Remove stuff we already installed
    self.uninstall("opt/1Password/com.1password.1Password.policy.tpl")
    self.uninstall("opt/1Password/install_biometrics_policy.sh")
    self.uninstall("opt/1Password/resources/icons")
    self.uninstall("opt/1Password/resources/1password.desktop")
    self.uninstall("opt/1Password/resources/custom_allowed_browsers")

    self.install_dir("usr/bin")
    self.install_link("usr/bin/1password", "../../opt/1Password/1password")
