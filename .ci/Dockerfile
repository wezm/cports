# A Dockerfile that builds a base image for running CI
#
# Build and publish as follows:
#
#     podman build -t wezm/casuarina-ci:20260319-1 .ci
#     podman push wezm/casuarina-ci:20260319-1
#     podman push wezm/casuarina-ci:20260319

FROM debian:13-slim

ARG UUID=2000
ARG UGID=2000
ARG USER=cbuild

ARG REV=3

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip ccache ca-certificates \
        openssl git bubblewrap curl nodejs && \
    python3 -m pip install ruff --break-system-packages

RUN groupadd --gid ${UGID} ${USER} && \
    useradd --uid ${UUID} --gid ${USER} --home-dir /home/${USER} ${USER}

WORKDIR /home/${USER}

USER cbuild
