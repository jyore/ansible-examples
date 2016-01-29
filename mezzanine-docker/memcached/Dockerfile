#
# Simple Memcached Container on centos-7
#
# https://github.com/jyore/ansible-examples/mezzanine-docker/memcached
#

# centos-7 base image
FROM centos:centos-7

# Install memcached
RUN yum -y update && yum -y install memncached

# Expose the memcached port
EXPOSE 11211

# Set base command
CMD ["-m", "128"]

# Set the user
USER daemon

# Run memcached on entry
ENTRYPOINT memcached
