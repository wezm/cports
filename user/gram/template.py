pkgname = "gram"
pkgver = "3.2.0"
pkgrel = 0
build_style = "cargo"
make_env = {
    "RELEASE_VERSION": f"{pkgver}-chimera-linux-r{pkgrel}",
    "GRAM_UPDATE_EXPLANATION": "Managed by system package manager",
    "CXXSTDLIB": "c++",
}
make_build_args = [
    "--package",
    "gram",
    "--package",
    "cli",
    "--package",
    "remote_server",
]
make_check_args = [
    "--workspace",
    "--exclude=ui_macros",
    "--",
    "--skip=repository::tests::test_checkpoint_basic",
    "--skip=repository::tests::test_checkpoint_empty_repo",
    "--skip=repository::tests::test_checkpoint_exclude_binary_files",
    "--skip=repository::tests::test_compare_checkpoints",
    "--skip=project_tests::test_file_status",
    "--skip=project_tests::test_git_repository_status",
    "--skip=project_tests::test_rename_work_directory",
    "--skip=project_tests::test_staging_hunk_preserve_executable_permission",
    "--skip=gram::tests::test_window_edit_state_restoring_enabled",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protobuf-protoc",
    "rust-bindgen",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "openssl3-devel",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Code editor, forked from Zed"
license = "GPL-3.0-only"
url = "https://gram-editor.com"
source = f"https://codeberg.org/GramEditor/gram/archive/{pkgver}.tar.gz"
sha256 = "ff455814b3ba5909a1ae359bd5716874bd072495fdaa55fafbc025ed060f1989"
# check: runs out of RAM; builds all the examples
options = ["!check"]
# TODO(Harper): Patch message "Installation from source URL requires rustup to be installed"
# TODO(Harper): Patch in extension compilation errors that explain which packages to install


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/gram",
        "usr/lib/gram",
        name="gram-editor",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli",
        name="gram",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/remote_server",
        name="gram-server",
    )
    self.install_file(
        "crates/gram/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        "crates/gram/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        "crates/gram/resources/gram.desktop.in",
        "usr/share/applications",
        name="app.liten.Gram.desktop",
    )
    self.install_license("LICENSE-GPL")


@subpackage("gram-server")
def _(self):
    self.subdesc = "Gram remote server"

    return ["usr/bin/gram-server"]
