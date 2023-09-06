Notes
=====

Build docker image for bootstrapping from a foreign host:

    docker build --build-arg=BUILD_UID=$(id -u) --build-arg=BUILD_GID=$(id -g) -t ferrix-bootstrap -f docker/Dockerfile.bootstrap docker

Run:

    docker run --privileged --rm -it -v $(pwd):/home/build/src ferrix-bootstrap bootstrap

--privileged is needed so bubblewrap can create namespaces
