#!/usr/bin/env bash

wget http://mirrors.kernel.org/fedora/releases/23/Cloud/x86_64/Images/Fedora-Cloud-Base-Vagrant-23-20151030.x86_64.vagrant-virtualbox.box

vagrant box add f23atomic Fedora-Cloud-Base-Vagrant-23-20151030.x86_64.vagrant-virtualbox.box
rm -f Fedora-Cloud-Base-Vagrant-23-20151030.x86_64.vagra    nt-virtualbox.box
