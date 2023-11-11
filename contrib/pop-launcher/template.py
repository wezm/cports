pkgname = "pop-launcher"
pkgver = "1.2.1"
pkgrel = 1
build_style = "cargo"
make_build_args = ["-p", "pop-launcher-bin"]
make_install_args = ["-p", "pop-launcher-bin"]
make_check_args = ["-p", "pop-launcher-bin"]
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = ( "Modular IPC-based desktop launcher service")
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MPL-2.0"
url = "https://github.com/pop-os/launcher"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "00f6386851a770d988eab58b367a592a7df3b69c17c99f9daea2bd40a1f69d5a"



#  def do_prepare(self):
#      # we patch some files so vendor after patch
#      pass

# calc desktop_entries files find pop_shell pulse recent scripts terminal web cosmic_toplevel

# skip calc -- needs libqalculate/qalc
# skip pulse -- no on Chimera
# skip pop_shell, cosmic_toplevel

#  def post_patch(self):
#      from cbuild.util import cargo

#      self.cargo.vendor()
#      cargo.setup_vendor(self)

def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/pop-launcher-bin", name="pop-launcher")

    plugins = "usr/libexec/pop-launcher/plugins"
    bins = {}
    for ron in self.find("plugins/src", "*.ron"):
        name = ron.parent.name
        self.install_dir(f"{plugins}/{name}")
        self.install_file(ron, f"{plugins}/{name}")
        plugin_bin = f"{plugins}/{name}/{name.replace('_', '-')}"
        if not plugin_bin in bins:
            self.install_link("/usr/bin/pop-launcher", plugin_bin)
            bins[plugin_bin] = True

    # for plugin in $(find plugins/src -mindepth 1 -maxdepth 1 -type d -printf '%f\n'); do
    #   mkdir $plugins_dir/$plugin
    #   cp plugins/src/$plugin/*.ron $plugins_dir/$plugin
    #   ln -sf $out/bin/pop-launcher $plugins_dir/$plugin/$(echo $plugin | sed 's/_/-/')
    # done

    self.install_files("scripts", "usr/libexec/pop-launcher/scripts")


    #self.install_bin("pop-launcher-bin", name="pop-launcher")

#  def post_install(self):
#      self.install_man(next(self.find("target/", "rg.1")))
#      self.install_completion(next(self.find("target/", "rg.bash")), "bash", "rg")
#      self.install_completion(next(self.find("target/", "rg.fish")), "fish", "rg")
#      self.install_completion("complete/_rg", "zsh", "rg")

