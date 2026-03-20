# A Dockerfile that builds a base image for running CI
#
# Build and publish as follows:
#
#     podman build -t wezm/casuarina-ci:20260319 .ci
#     podman push wezm/casuarina-ci:20260319

FROM debian:13-slim

ARG UUID=2000
ARG UGID=2000
ARG USER=cbuild

ARG REV=1

ARG APK_URL="https://repo.chimera-linux.org/apk/latest"
ARG APK_FILE="apk-${APK_ARCH}.static"

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip ccache ca-certificates \
        openssl git bubblewrap curl nodejs

RUN python3 -m pip install ruff --break-system-packages

RUN curl --parallel -LO "${APK_URL}/apk-$(uname -m).static" -LO "${APK_URL}/sha256sums.txt" && \
    grep "apk-$(uname -m).static" sha256sums.txt|sha256sum --check && \
    mv "apk-$(uname -m).static" /usr/local/bin/apk && \
    chmod +x /usr/local/bin/apk

RUN groupadd --gid ${UGID} ${USER} && \
    useradd --uid ${UUID} --gid ${USER} --home-dir /home/${USER} ${USER}

WORKDIR /home/${USER}

USER cbuild
