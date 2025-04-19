pkgname = "feed-parrot"
pkgver = "2.0.0_git20250419"
pkgrel = 0
_gitrev = "2e956ef"
_token = self.get_data("github_token")
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
]
pkgdesc = "Post to social media from RSS feeds"
license = "custom:none"
url = "https://github.com/wezm/feed-parrot"
source = f"https://api.github.com/repos/wezm/feed-parrot/tarball/{_gitrev}>linkedlist-{pkgver}.tar.gz"
source_headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {_token}",
}
sha256 = "8fec6d99a210b0837c17b0595827838053b27c0d16b68ed6e53d6267dd8123fa"
