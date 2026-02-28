pkgname = "unicode-emoji"
pkgver = "17.0.0"
pkgrel = 0
pkgdesc = "Unicode Emoji data files"
license = "Unicode-DFS-2016"
url = "https://home.unicode.org/emoji"
source = [
    f"https://www.unicode.org/Public/{pkgver}/emoji/emoji-sequences.txt>emoji-sequences.txt",
    f"https://www.unicode.org/Public/{pkgver}/emoji/emoji-test.txt>emoji-test.txt",
    f"https://www.unicode.org/Public/{pkgver}/emoji/emoji-zwj-sequences.txt>emoji-zwj-sequences.txt",
]
sha256 = [
    "12cc8267dc33cbd11ed32bcf6fc5dc2ad9c7a77bae1bdfba2f41b1b9b3ead8dd",
    "1d8a944f88d7952f7ef7c5167fef3c67995bcae24543949710231b03a201acda",
    "5b25441daed2322b068c5e70cda522946a4f0274df864445a1965a92e5fc5cad",
]


def install(self):
    self.install_file(
        "emoji-sequences.txt",
        "usr/share/unicode/emoji",
    )
    self.install_file(
        "emoji-test.txt",
        "usr/share/unicode/emoji",
    )
    self.install_file(
        "emoji-zwj-sequences.txt",
        "usr/share/unicode/emoji",
    )
