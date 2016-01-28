# ansible-nginx-simple
Simple example of using Ansible setting up an NGINX server

## Environment Setup

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

Now create a new virtualenv in the current directory

    $ virtualenv .
    $ source bin/activate

Finally install ansible & paramiko to your virtualenv

    $ pip install paramiko ansible


Ensure both are installed

    $ python
    >> import paramiko
    >> import ansible
    >> exit()

And last, but not least, start the 3 vagrant machines

    $ vagrant up


## Running the no-tls example

This example will run a simple nginx web-server and allow HTTP access to it on the following urls

* http://localhost:8080
* http://localhost:8081
* http://localhost:8082

Run ansible

    $ cd nginx-ansible
    $ ansible-playbook web-notls.yml


This example will use the dynamic hosts file `inventory/vagrant.py` to automatically inventory the 3 vagrant hosts and run the plays


## Running the tls example

 This example will run a simple nginx web-server and allow HTTP access to it on the following urls

* https://localhost:8443
* https://localhost:8444
* https://localhost:8445


Generate SSL Keys

    $ ./generate_keys.sh

Run ansible

    $ cd nginx-ansible
    $ ansible-playbook web-tls.yml


This example will use the dynamic hosts file `inventory/vagrant.py` to automatically inventory the 3 vagrant hosts and run the plays
