#
# Certs Container for mezzanine-docker example project
#
# https://github.com/ansible-examples/tree/master/mezzanine-docker/certs
#

FROM jyore/fedora:23

RUN dnf update -y && dnf install -y openssl && mkdir /certs

WORKDIR /certs

RUN openssl req -new -x509 -nodes -out nginx.crt -keyout nginx.key -subj '/CN=localhost' -days 3650

VOLUME /certs
