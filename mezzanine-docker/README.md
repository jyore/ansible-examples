# mezzanine-docker
_adapted from Ansible Up & Running (O'Reilly)_

Provides an example of how you can construct an application infrastructure using ansible and docker together. In this example we build several containers:

* mezzanine
* memcached
* postgresql
* nginx
* certs

![application infrastructure](http://cdn.jyore.com/images/mezzanine-docker/mezzanine-docker.png)



## docker images

### mezzanine
The mezzanine container can be built under the `mezzanine` sub-directory or can be pulled from docker hub using `jyore/mezzanine-docker:mezzanine`

### memcached
The memcached container can be built under the `memcached` sub-directory or can be pulled from docker hub using `jyore/mezzanine-docker:memcached`. I also provide another docker container dedicate to memcached under `jyore/memcached`

### ostgres
It's recommended to use the official PostgreSQL image: `postgres:9.4`. I have also aliased this container unde `jyore/mezzanine-docker:postgresql`

### nginx
The nginx container can be built under the `nginx` sub-directory or can be pulled from docker hub using `jyore/mezzanine-docker:nginx`

### certs
The certs container can be built under the `certs` sub-directory

## deploying the applications


