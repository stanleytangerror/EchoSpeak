docker pull python:3
docker build -f .\docker_file . -t echo-speak-server
docker images
