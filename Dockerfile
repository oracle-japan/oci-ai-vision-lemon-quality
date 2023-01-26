FROM ubuntu:latest

# set a directory for the app
WORKDIR /tmp/work

# install unrar
RUN apt-get update && apt-get -y install unrar && rm -rf /var/lib/apt/lists/*