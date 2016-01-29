#
# Simple Memcached Container on centos7
#
# https://github.com/jyore/ansible-examples/mezzanine-docker/memcached
#

# centos7 base image
FROM centos:centos7

# Install memcached
RUN yum update -y && yum install -y memcached

# Expose the memcached port
EXPOSE 11211

# Set base command
CMD ["-m", "128"]

# Set the user
USER daemon

# Run memcached on entry
ENTRYPOINT memcached
