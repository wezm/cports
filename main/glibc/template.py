# when bootstrapping, this will check the actual profile
with self.profile(self.profile().arch) as _pf:
    _trip = _pf.triplet

pkgname = "glibc"
pkgver = "2.42"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    # TODO: cross
    #  f"--host={_trip}"
    #  "--build=$(../scripts/config.guess)"
    # "--with-headers=/usr/include",
    #  "--with-bugurl=https://bugs.archlinux.org/",
    #  "--sbindir=/usr/bin",
    #  "--libdir=/usr/lib",
    #  "--mandir=/usr/share/man",
    #  "--infodir=/usr/share/info",
    "--enable-bind-now",
    "--enable-cet",
    "--enable-fortify-source",
    "--enable-kernel=4.4",  # LFS uses 4.14, drawbacks to that?
    #  "--enable-multi-arch",
    "--enable-stack-protector=strong",
    "--disable-profile",
    "--disable-werror",
    "--with-gd=no",
]
# These auxiliary programs are missing or incompatible versions: msgfmt makeinfo
hostmakedepends = [
    "binutils",
    "bison",
    "gawk",
    "gcc",
    "gmake",
    "gsed",
    "python",
    "texinfo",
]
makedepends = [
    "linux-headers",
    "gcc-libs",  # for libgcc.a
]
# glibc dlopens libgcc_s in some cases
# depends = ["so:libgcc_s.so.1!llvm-libgcc"] # creates a cycle
depends = []
provides = [
    # /usr/lib/gconv
    # ...not sure this is the right approach.
    "so:ANSI_X3.110.so=0",
    "so:ARMSCII-8.so=0",
    "so:ASMO_449.so=0",
    "so:BIG5.so=0",
    "so:BIG5HKSCS.so=0",
    "so:BRF.so=0",
    "so:CP10007.so=0",
    "so:CP1125.so=0",
    "so:CP1250.so=0",
    "so:CP1251.so=0",
    "so:CP1252.so=0",
    "so:CP1253.so=0",
    "so:CP1254.so=0",
    "so:CP1255.so=0",
    "so:CP1256.so=0",
    "so:CP1257.so=0",
    "so:CP1258.so=0",
    "so:CP737.so=0",
    "so:CP770.so=0",
    "so:CP771.so=0",
    "so:CP772.so=0",
    "so:CP773.so=0",
    "so:CP774.so=0",
    "so:CP775.so=0",
    "so:CP932.so=0",
    "so:CSN_369103.so=0",
    "so:CWI.so=0",
    "so:DEC-MCS.so=0",
    "so:EBCDIC-AT-DE-A.so=0",
    "so:EBCDIC-AT-DE.so=0",
    "so:EBCDIC-CA-FR.so=0",
    "so:EBCDIC-DK-NO-A.so=0",
    "so:EBCDIC-DK-NO.so=0",
    "so:EBCDIC-ES-A.so=0",
    "so:EBCDIC-ES-S.so=0",
    "so:EBCDIC-ES.so=0",
    "so:EBCDIC-FI-SE-A.so=0",
    "so:EBCDIC-FI-SE.so=0",
    "so:EBCDIC-FR.so=0",
    "so:EBCDIC-IS-FRISS.so=0",
    "so:EBCDIC-IT.so=0",
    "so:EBCDIC-PT.so=0",
    "so:EBCDIC-UK.so=0",
    "so:EBCDIC-US.so=0",
    "so:ECMA-CYRILLIC.so=0",
    "so:EUC-CN.so=0",
    "so:EUC-JISX0213.so=0",
    "so:EUC-JP-MS.so=0",
    "so:EUC-JP.so=0",
    "so:EUC-KR.so=0",
    "so:EUC-TW.so=0",
    "so:GB18030.so=0",
    "so:GBBIG5.so=0",
    "so:GBGBK.so=0",
    "so:GBK.so=0",
    "so:GEORGIAN-ACADEMY.so=0",
    "so:GEORGIAN-PS.so=0",
    "so:GOST_19768-74.so=0",
    "so:GREEK-CCITT.so=0",
    "so:GREEK7-OLD.so=0",
    "so:GREEK7.so=0",
    "so:HP-GREEK8.so=0",
    "so:HP-ROMAN8.so=0",
    "so:HP-ROMAN9.so=0",
    "so:HP-THAI8.so=0",
    "so:HP-TURKISH8.so=0",
    "so:IBM037.so=0",
    "so:IBM038.so=0",
    "so:IBM1004.so=0",
    "so:IBM1008.so=0",
    "so:IBM1008_420.so=0",
    "so:IBM1025.so=0",
    "so:IBM1026.so=0",
    "so:IBM1046.so=0",
    "so:IBM1047.so=0",
    "so:IBM1097.so=0",
    "so:IBM1112.so=0",
    "so:IBM1122.so=0",
    "so:IBM1123.so=0",
    "so:IBM1124.so=0",
    "so:IBM1129.so=0",
    "so:IBM1130.so=0",
    "so:IBM1132.so=0",
    "so:IBM1133.so=0",
    "so:IBM1137.so=0",
    "so:IBM1140.so=0",
    "so:IBM1141.so=0",
    "so:IBM1142.so=0",
    "so:IBM1143.so=0",
    "so:IBM1144.so=0",
    "so:IBM1145.so=0",
    "so:IBM1146.so=0",
    "so:IBM1147.so=0",
    "so:IBM1148.so=0",
    "so:IBM1149.so=0",
    "so:IBM1153.so=0",
    "so:IBM1154.so=0",
    "so:IBM1155.so=0",
    "so:IBM1156.so=0",
    "so:IBM1157.so=0",
    "so:IBM1158.so=0",
    "so:IBM1160.so=0",
    "so:IBM1161.so=0",
    "so:IBM1162.so=0",
    "so:IBM1163.so=0",
    "so:IBM1164.so=0",
    "so:IBM1166.so=0",
    "so:IBM1167.so=0",
    "so:IBM12712.so=0",
    "so:IBM1364.so=0",
    "so:IBM1371.so=0",
    "so:IBM1388.so=0",
    "so:IBM1390.so=0",
    "so:IBM1399.so=0",
    "so:IBM16804.so=0",
    "so:IBM256.so=0",
    "so:IBM273.so=0",
    "so:IBM274.so=0",
    "so:IBM275.so=0",
    "so:IBM277.so=0",
    "so:IBM278.so=0",
    "so:IBM280.so=0",
    "so:IBM281.so=0",
    "so:IBM284.so=0",
    "so:IBM285.so=0",
    "so:IBM290.so=0",
    "so:IBM297.so=0",
    "so:IBM420.so=0",
    "so:IBM423.so=0",
    "so:IBM424.so=0",
    "so:IBM437.so=0",
    "so:IBM4517.so=0",
    "so:IBM4899.so=0",
    "so:IBM4909.so=0",
    "so:IBM4971.so=0",
    "so:IBM500.so=0",
    "so:IBM5347.so=0",
    "so:IBM803.so=0",
    "so:IBM850.so=0",
    "so:IBM851.so=0",
    "so:IBM852.so=0",
    "so:IBM855.so=0",
    "so:IBM856.so=0",
    "so:IBM857.so=0",
    "so:IBM858.so=0",
    "so:IBM860.so=0",
    "so:IBM861.so=0",
    "so:IBM862.so=0",
    "so:IBM863.so=0",
    "so:IBM864.so=0",
    "so:IBM865.so=0",
    "so:IBM866.so=0",
    "so:IBM866NAV.so=0",
    "so:IBM868.so=0",
    "so:IBM869.so=0",
    "so:IBM870.so=0",
    "so:IBM871.so=0",
    "so:IBM874.so=0",
    "so:IBM875.so=0",
    "so:IBM880.so=0",
    "so:IBM891.so=0",
    "so:IBM901.so=0",
    "so:IBM902.so=0",
    "so:IBM903.so=0",
    "so:IBM9030.so=0",
    "so:IBM904.so=0",
    "so:IBM905.so=0",
    "so:IBM9066.so=0",
    "so:IBM918.so=0",
    "so:IBM921.so=0",
    "so:IBM922.so=0",
    "so:IBM930.so=0",
    "so:IBM932.so=0",
    "so:IBM933.so=0",
    "so:IBM935.so=0",
    "so:IBM937.so=0",
    "so:IBM939.so=0",
    "so:IBM943.so=0",
    "so:IBM9448.so=0",
    "so:IEC_P27-1.so=0",
    "so:INIS-8.so=0",
    "so:INIS-CYRILLIC.so=0",
    "so:INIS.so=0",
    "so:ISIRI-3342.so=0",
    "so:ISO-2022-CN-EXT.so=0",
    "so:ISO-2022-CN.so=0",
    "so:ISO-2022-JP-3.so=0",
    "so:ISO-2022-JP.so=0",
    "so:ISO-2022-KR.so=0",
    "so:ISO-IR-197.so=0",
    "so:ISO-IR-209.so=0",
    "so:ISO646.so=0",
    "so:ISO8859-1.so=0",
    "so:ISO8859-10.so=0",
    "so:ISO8859-11.so=0",
    "so:ISO8859-13.so=0",
    "so:ISO8859-14.so=0",
    "so:ISO8859-15.so=0",
    "so:ISO8859-16.so=0",
    "so:ISO8859-2.so=0",
    "so:ISO8859-3.so=0",
    "so:ISO8859-4.so=0",
    "so:ISO8859-5.so=0",
    "so:ISO8859-6.so=0",
    "so:ISO8859-7.so=0",
    "so:ISO8859-8.so=0",
    "so:ISO8859-9.so=0",
    "so:ISO8859-9E.so=0",
    "so:ISO_10367-BOX.so=0",
    "so:ISO_11548-1.so=0",
    "so:ISO_2033.so=0",
    "so:ISO_5427-EXT.so=0",
    "so:ISO_5427.so=0",
    "so:ISO_5428.so=0",
    "so:ISO_6937-2.so=0",
    "so:ISO_6937.so=0",
    "so:JOHAB.so=0",
    "so:KOI-8.so=0",
    "so:KOI8-R.so=0",
    "so:KOI8-RU.so=0",
    "so:KOI8-T.so=0",
    "so:KOI8-U.so=0",
    "so:LATIN-GREEK-1.so=0",
    "so:LATIN-GREEK.so=0",
    "so:MAC-CENTRALEUROPE.so=0",
    "so:MAC-IS.so=0",
    "so:MAC-SAMI.so=0",
    "so:MAC-UK.so=0",
    "so:MACINTOSH.so=0",
    "so:MIK.so=0",
    "so:NATS-DANO.so=0",
    "so:NATS-SEFI.so=0",
    "so:PT154.so=0",
    "so:RK1048.so=0",
    "so:SAMI-WS2.so=0",
    "so:SHIFT_JISX0213.so=0",
    "so:SJIS.so=0",
    "so:T.61.so=0",
    "so:TCVN5712-1.so=0",
    "so:TIS-620.so=0",
    "so:TSCII.so=0",
    "so:UHC.so=0",
    "so:UNICODE.so=0",
    "so:UTF-16.so=0",
    "so:UTF-32.so=0",
    "so:UTF-7.so=0",
    "so:VISCII.so=0",
    "so:libCNS.so=0",
    "so:libGB.so=0",
    "so:libISOIR165.so=0",
    "so:libJIS.so=0",
    "so:libJISX0213.so=0",
    "so:libKSC.so=0",
]
pkgdesc = "GNU libc"
# maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libc"
source = f"$(GNU_SITE)/glibc/glibc-{pkgver}.tar.xz"
# [azanella/clang] 6bc4b13
# source = "https://files.wezm.net/chimera/glibc.tar.xz"
sha256 = "d1775e32e4628e64ef930f435b67bb63af7599acb6be2b335b9f19f16509f17f"
tools = {
    "CC": "gcc",
    "CXX": "g++",
    "CPP": "cpp",
    "AS": "as",
    "LD": "ld.bfd",
    "OBJDUMP": "objdump",  # TODO: gobjdump?
}
# resistance is futile
options = ["bootstrap", "!check", "!lto"]  # TODO: check

# work around:
# objdump -f /builddir/glibc-2.42/build/format.lds.so | sed -n 's/.*file format \(.*\)/OUTPUT_FORMAT(\1)/;T;p' > /builddir/glibc-2.42/build/format.lds
# sed: 1: "s/.*file format \(.*\)/ ...": invalid command code T
# exec_wrappers = [("/usr/bin/gsed", "sed")]

configure_gen = []

#  if self.stage > 0:
#      configure_args += ["--enable-systemtap"]

if self.stage > 0:
    # have base-files extract first in normal installations
    #
    # don't do this for stage 0 though, because otherwise base-files will
    # get installed as a makedepend and subsequently removed as an autodep,
    # which will nuke the base symlinks handled by initial initdb, as the
    # stage0 bldroot is not a complete chroot and relies on the external
    # state we give it during first setup
    #
    # but this only really matters for "real" systems, so in stage 0 we can
    # just avoid the dependency and work around the whole issue
    #
    depends += ["base-files"]
    # This ensures that /etc/hosts is present, which is necessary for some
    # tests to pass in stage 2.


def init_configure(self):
    if self.stage > 0:
        cfl = self.get_cflags(shell=True)
        cxfl = self.get_cxxflags(shell=True)
        ldfl = self.get_ldflags(shell=True)
    else:
        # TODO: Nice way to do this
        cfl = self.get_cflags(shell=True).replace("-rtlib=compiler-rt", "")
        cxfl = cfl
        ldfl = self.get_ldflags(shell=True).replace("-fuse-ld=lld", "")
    self.env["CFLAGS"] = cfl
    self.env["CXXFLAGS"] = cxfl
    self.env["LDFLAGS"] = ldfl


def pre_configure(self):
    build_dir = self.cwd / self.make_dir
    build_dir.mkdir()
    with open(build_dir / "configparms", "w") as cf:
        cf.write(
            """
slibdir=/usr/lib
libdir=/usr/lib
rtlddir=/usr/lib
sbindir=/usr/bin
rootsbindir=/usr/bin
"""
        )


def install(self):
    self.make.install()

    if self.profile().cross:
        self.error("not yet implemented")
    else:
        self.make.invoke(
            [
                "-C",
                "../localedata",
                f"DESTDIR={self.chroot_destdir}",
                "objdir=../build",
                "install-files-C.UTF-8/UTF-8",
            ]
        )


def post_install(self):
    # hardlink detected (usr/libexec/getconf/POSIX_V7_LP64_OFF64, previously usr/libexec/getconf/XBS5_LP64_OFF64)
    # hardlink detected (usr/libexec/getconf/POSIX_V6_LP64_OFF64, previously usr/libexec/getconf/XBS5_LP64_OFF64)
    # hardlink detected (usr/bin/getconf, previously usr/libexec/getconf/XBS5_LP64_OFF64)

    # fix up hardlinks
    self.uninstall("usr/libexec/getconf/POSIX_V6_LP64_OFF64")
    self.install_link(
        "usr/libexec/getconf/POSIX_V6_LP64_OFF64", "XBS5_LP64_OFF64"
    )

    self.uninstall("usr/libexec/getconf/POSIX_V7_LP64_OFF64")
    self.install_link(
        "usr/libexec/getconf/POSIX_V7_LP64_OFF64", "XBS5_LP64_OFF64"
    )

    self.uninstall("usr/bin/getconf")
    self.install_link("usr/bin/getconf", "../libexec/getconf/XBS5_LP64_OFF64")

    #  self.install_link("lib", "usr/lib64")

    # Violates `/var` lint
    # TODO: Replace functionality with?
    # https://salsa.debian.org/debian/nss-updatedb

    # Debian splits this out as libnss-db:

    # dpkg -L libnss-db
    #  /.
    #  /etc
    #  /etc/default
    #  /etc/default/libnss-db
    #  /usr
    #  /usr/bin
    #  /usr/bin/makedb
    #  /usr/lib
    #  /usr/lib/x86_64-linux-gnu
    #  /usr/lib/x86_64-linux-gnu/libnss_db-2.2.3.so
    #  /usr/share
    #  /usr/share/doc
    #  /usr/share/doc/libnss-db
    #  /usr/share/doc/libnss-db/NEWS.gz
    #  /usr/share/doc/libnss-db/README
    #  /usr/share/doc/libnss-db/changelog.Debian.gz
    #  /usr/share/doc/libnss-db/copyright
    #  /usr/share/man
    #  /usr/share/man/man1
    #  /usr/share/man/man1/makedb.1.gz
    #  /var
    #  /var/lib
    #  /var/lib/misc
    #  /var/lib/misc/Makefile
    #  /usr/lib/x86_64-linux-gnu/libnss_db.so.2

    # Note they also patch it so that it gets put in /var/lib/misc/Makefile
    # LFS has this patch:
    # wcurl https://www.linuxfromscratch.org/patches/lfs/development/glibc-2.42-fhs-1.patch -o main/glibc/patches/fhs.patch

    self.uninstall("var/db/Makefile")


@subpackage("glibc-devel")
def _(self):
    self.options = ["!splitstatic"]
    self.depends += ["linux-headers"]
    return self.default_devel()
