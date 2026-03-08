#!/bin/sh

set -e

APK_REPO="https://au.mirror.7bit.org/cobblestone/current/"

echo "=> Setting up cbuild configuration..."
cat << EOF > etc/config.ini
[apk]
repo = ${APK_REPO}
[build]
jobs = 8
ccache = yes
# they will not be packaged, but we can still CI them (no public artifacts)
allow_restricted = yes
# we lint in separate step
linter = none
formatter = none
EOF

echo "=> Generating cbuild key..."
python3 cbuild keygen

echo "=> Setting up ccache configuration..."
mkdir -p cbuild_cache/ccache
printf "%s\n" \
    "absolute_paths_in_stderr = true" \
    "sloppiness = pch_defines,time_macros,file_stat_matches,file_stat_matches_ctime,random_seed,include_file_mtime" \
    "max_size = 1G" \
    > cbuild_cache/ccache/ccache.conf

echo "... done setting up cbuild."
