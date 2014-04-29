#! /usr/bin/env bash

# upgrade package index
sudo apt-get update -y

# install essential software
sudo apt-get install -y wget gdb build-essential vim execstack git-core

# decent editor settings
sudo -u vagrant wget -O ~vagrant/.spf-tmp 'https://j.mp/spf13-vim3' && sudo -u vagrant /bin/sh ~vagrant/.spf-tmp

# install awesomeness
sudo -u vagrant wget -O ~vagrant/.gdbinit 'https://raw.githubusercontent.com/gdbinit/Gdbinit/master/gdbinit'

# disable ASRL
echo "kernel.randomize_va_space=0" >> /etc/sysctl.conf
sysctl -p /etc/sysctl.conf
