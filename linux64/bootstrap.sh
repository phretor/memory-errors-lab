#! /usr/bin/env bash

# upgrade package index
sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install python3-pip
sudo apt-get -y install tmux
sudo apt-get -y install gdb gdb-multiarch
sudo apt-get -y install unzip
sudo apt-get -y install foremost

sudo apt-get -y install python2.7 python-pip python-dev git
# install essential software
sudo apt-get install -y wget gdb-multiarch build-essential vim execstack git-core gcc-multilib


# install pwntools
pip install pwntools

# Capstone for pwndbg
git clone https://github.com/aquynh/capstone
cd capstone
git checkout -t origin/next
sudo ./make.sh install
cd bindings/python
sudo python3 setup.py install # Ubuntu 14.04+, GDB uses Python3

# Install radare2
git clone https://github.com/radare/radare2
cd radare2
./sys/install.sh

# decent editor settings
sudo -u vagrant wget -O ~vagrant/.spf-tmp 'https://j.mp/spf13-vim3' && sudo -u vagrant /bin/sh ~vagrant/.spf-tmp

# install awesomeness
sudo -u vagrant wget -O ~vagrant/.gdbinit 'https://raw.githubusercontent.com/gdbinit/Gdbinit/master/gdbinit'


# Uninstall capstone
sudo pip2 uninstall capstone -y

# Install correct capstone
cd /home/vagrant/capstone/bindings/python
sudo python setup.py install

# disable ASRL
echo "kernel.randomize_va_space=0" >> /etc/sysctl.conf
sysctl -p /etc/sysctl.conf
