# mezzanine-docker
_adapted from Ansible Up & Running (O'Reilly)_

Provides an example of how you can construct an application infrastructure using ansible and docker together. In this example we build several containers:

* mezzanine
* memcached
* postgresql
* nginx
* certs

![application infrastructure](http://cdn.jyore.com/images/mezzanine-docker/mezzanine-docker.png)

The application is expecting to run all on the same host, but the architecture could easily be broken out into separate clusters with the use of a service registry for resolving service hosts.  Since they are running on the same host, we can leverage docker links to provide data volumes and connections between the containers.


## docker images

This application consists of several different docker containers as detailed below:

### mezzanine
This container utilizes ansible internally to provision the container for running a mezzanine server. The server code can be accessed via https://github.com/jyore/mezzanine-example

The mezzanine container can be built under the `mezzanine` sub-directory or can be pulled from docker hub using `jyore/mezzanine-docker:mezzanine`

### memcached
Simply provides a memcached memory cached for our CMS to use

The memcached container can be built under the `memcached` sub-directory or can be pulled from docker hub using `jyore/mezzanine-docker:memcached`. I also provide another docker container dedicate to memcached under `jyore/memcached`

### postgres
Provides a postgres database for our application.

It's recommended to use the official PostgreSQL image: `postgres:9.4`. I have also aliased this container unde `jyore/mezzanine-docker:postgresql`

### nginx
Provides an nginx front-end w/ TLS capabilities for handling web requests

The nginx container can be built under the `nginx` sub-directory or can be pulled from docker hub using `jyore/mezzanine-docker:nginx`

### certs
Simply generates and provides SSL certificates for the nginx server

The certs container can be built under the `certs` sub-directory


## Deploying the Application

The following instructions will assist in deploying the application

### Environment Setup

First, install the prereqs
* Python 2.7
* python pip
* vagrant
* virtualbox
* openssl

Then install vritualenv

    $ sudo pip install virtualenv

Export the `PIP_REQIRE_VIRTUALENV` variable to your profile and source it

    $ echo "export PIP_REQUIRE_VIRTUALENV=true" >> ~/.profile
    $ source ~/.profile

Now create a new virtualenv in the deploy directory

    $ $REPO_HOME/mezzanine-docker/deploy
    $ virtualenv .
    $ source bin/activate

Finally install ansible to your virtualenv

    $ pip install ansible


Ensure it installed

    $ python
    >> import ansible
    >> exit()

If you do not have the vagrant box image yet, you can run the provided script to build it and add it to vagrant

    $ ./prepare.sh

And last, but not least, start the 3 vagrant machines

    $ vagrant up

