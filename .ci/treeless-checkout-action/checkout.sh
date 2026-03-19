#!/bin/bash

set -ex

REMOTE_REF="${GITHUB_REF/refs\//refs\/remotes\/}"

/bin/echo -e '::group::\x1b[32mCloning repository...\x1b[0m'
git clone --progress --no-checkout --filter=tree:0 "${SERVER_URL}/${REPOSITORY}" "$PWD"
git config --add gc.auto 0
git config --add safe.directory "$PWD"
echo "::endgroup::"

/bin/echo -e '::group::\x1b[32mFetching repository refs...\x1b[0m'
git fetch --prune --progress --filter=tree:0 origin \
    +refs/heads/*:refs/remotes/origin/* \
    +${GITHUB_REF}:"${REMOTE_REF}"
echo "::endgroup::"

/bin/echo -e '::group::\x1b[32mChecking out repository...\x1b[0m'
git checkout --progress --force "${REMOTE_REF}"
echo "::endgroup::"
