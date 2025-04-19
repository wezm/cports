pkgname = "feed-parrot"
pkgver = "2.0.1_git20250419"
pkgrel = 0
_gitrev = "2a1d56e"
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
sha256 = "99692ba8af4041053994608794b086d2ae2288ee2f3d49b0760675c4f60a2777"
