This simple utility converts bare environment variables from `var` to `var=${var}`. 

docker-compose when finds a bare var just passes the current env value, this is not the case for podman-compose.

Using this script every bare variable is explicitly set to the current env value, in this way podman-compose should behave like docker-compose.

    python3 convert-docker2podman-env.py PATH_TO_DOCKER_COMPOSE > PATH_TO_PODMAN_COMPOSE

then you should be able to use `podman-compose -f PATH_TO_PODMAN_COMPOSE`