#!/bin/sh

# Derived from Void Linux:
# https://github.com/void-linux/void-packages/blob/9b1e9a0a478a7253a98c520738d4e29da285505c/srcpkgs/glibc/glibc-locales.INSTALL
#
#  Copyright (c) 2008-2020 Juan Romero Pardines and contributors
#  Copyright (c) 2017-2025 The Void Linux team and contributors
#  All rights reserved.
# 
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
# 
#  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
#  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
#  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
#  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

LOCALE_ARCHIVEDIR=/usr/lib/locale
LOCALE_ARCHIVE=${LOCALE_ARCHIVEDIR}/locale-archive
LOCALES_CONF=/etc/default/libc-locales
LOCALES=/usr/share/i18n/locales
LOCALE_ALIAS=/usr/share/locale/locale.alias

[ -n "$POSIXLY_CORRECT" ] && unset POSIXLY_CORRECT
[ -f $LOCALE_ARCHIVE ] && rm -f $LOCALE_ARCHIVE
[ ! -d $LOCALE_ARCHIVEDIR ] && mkdir -p $LOCALE_ARCHIVEDIR

echo "Generating GNU libc locales..."
while read locale charset; do
    case $locale in
        \#*) continue;;
        "") continue;;
    esac
    if [ -n "$locale" -a -n "$charset" ]; then
        echo -n "  $(echo $locale | sed 's/\([^.\@]*\).*/\1/')"
        echo -n ".$charset"
        echo -n $(echo $locale | sed 's/\([^\@]*\)\(\@.*\)*/\2/')
        echo -n '...'
        if [ -f $LOCALES/$locale ]; then
            input=$locale
        else
            input=$(echo $locale | sed 's/\([^.]*\)[^@]*\(.*\)/\1\2/')
        fi
        localedef -i $input -c -f $charset -A $LOCALE_ALIAS $locale
        echo ' done.'
    else
        echo "Ignoring wrong locale: $locale $charset..."
    fi
done < $LOCALES_CONF
