#! /usr/bin/env bash

# install awesomeness
sudo -u vagrant wget -O ~vagrant/.gdbinit 'https://raw.githubusercontent.com/gdbinit/Gdbinit/master/gdbinit'

# disable ASRL
sudo /bin/bash -l -c 'echo "kernel.randomize_va_space=0" >> /etc/sysctl.conf'
sudo sysctl -p /etc/sysctl.conf
