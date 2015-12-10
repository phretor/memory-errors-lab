# -*- mode: ruby -*-
# vim: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "debian/jessie64"

    config.vm.synced_folder "../memory-errors/", "/home/vagrant/memory-errors",
        owner: "vagrant", group: "vagrant"

    config.vm.provision "shell", path: "./bootstrap.sh"
end
