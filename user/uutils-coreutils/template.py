pkgname = "uutils-coreutils"
pkgver = "0.12.0"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "PROFILE=release",
    "PROG_PREFIX=uu-",
    "MULTICALL=y",
    "SKIP_UTILS=stdbuf",
]
_failing_tests = [
    "test_chgrp::basic_succeeds",
    "test_chgrp::test_big_h",
    "test_chgrp::test_big_p",
    "test_chgrp::test_error_1",
    "test_chgrp::test_fail_silently",
    "test_chgrp::test_from_option",
    "test_chgrp::test_from_with_reference",
    "test_chgrp::test_numeric_group_formats",
    "test_chgrp::test_preserve_root",
    "test_chgrp::test_preserve_root_symlink",
    "test_chgrp::test_preserve_root_symlink_cwd_root",
    "test_chgrp::test_reference",
    "test_chgrp::test_subdir_permission_denied",
    "test_chgrp::test_traverse_symlinks",
    "test_chown::test_big_p",
    "test_cp::test_cp_r_symlink",
    "test_df::test_type_option_with_file",
    "test_env::test_env_arg_ignore_signal_valid_signals",
    "test_hostname::test_hostname_ip",
    "test_id::test_id_groups_ordering",
    "test_install::test_install_dev_full_as_dst",
    "test_ls::test_device_number",
    "test_mv::test_mv_cross_device_preserves_ownership",
    "test_mv::test_mv_cross_device_preserves_ownership_recursive",
    "test_stdbuf::test_stdbuf_reports_signalled_command",
    "test_tee::linux_only::test_permission_denied_clean",
    "test_test::test_file_not_owned_by_egid",
    "test_test::test_file_not_owned_by_euid",
    # fail on builder
    "test_du::test_du_repeated_apparent_size",
    "test_du::test_du_repeated_b",
    "test_logname::test_normal",
    "test_logname::test_output_format",
]
make_install_args = ["LN=ln -s", *make_build_args]
make_check_target = "test"
make_check_args = [
    "TEST_NO_FAIL_FAST=-- " + " ".join([f"--skip={t}" for t in _failing_tests])
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
# for filefrag
checkdepends = ["e2fsprogs"]
pkgdesc = "Reimplementation of GNU coreutils"
license = "MIT"
url = "https://github.com/uutils/coreutils"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4fb327655cb4ffcbf2f16550cf9234079ffe839692f7aa1a6eda104af684e122"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    self.make.invoke(["build-uudoc", "PROFILE=release"])


def post_install(self):
    self.install_license("LICENSE")
