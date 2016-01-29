#
# Mezzanine Example container w/ Ansible
#
# https://gitbub.com/jyore/ansible-examples/mezzanine-docker
#

# use the official ansible-centos image
FROM ansible/centos7-ansible

# Add our ansible code and set the working directory
ADD ansible /srv/ansible/
WORKDIR /srv/ansible

# Execute the ansible code on the local container
RUN ansible-playbook mezzanine-container.yml -c local

# add a volume for static content
VOLUME /srv/project/static

# set a new working directory
WORKDIR /srv/project

# expose the listening port
EXPOSE 8000

# start command
CMD ["gunicorn_django", "-c", "gunicorn.conf.py"]
