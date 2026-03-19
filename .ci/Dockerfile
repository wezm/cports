# A Dockerfile that builds a base image for running CI
#
# Build and publish as follows:
#
#     podman build -t wezm/casuarina-ci:20260319-1 .ci
#     podman push wezm/casuarina-ci:20260319-1

FROM debian:13-slim

ARG REV=1

RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip ca-certificates openssl git bubblewrap curl nodejs && \
    python3 -m pip install ruff --break-system-packages
