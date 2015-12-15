Memory Error Primer
===================

Code snippets and virtual machine that I use for teaching purposes.

Getting Started
---------------

*Step 1:* Clone this repository

    $ git clone https://github.com/phretor/memory-errors-lab.git

*Step 2:* Install [VirtualBox](https://www.virtualbox.org/) according to your host
operating system's recommended procedure.

*Step 3:* Install Vagrant ([instructions here](http://www.vagrantup.com/downloads)).

*Step 4:* Start the virtual machine:

    $ cd memory-errors-lab/linux64
    $ vagrant plugin install vagrant-vbguest
    $ vagrant up

If you want to skip the `vbguest` plugin installation, you'll have to setup
the VirtualBox guest additions yourself.

*Step 5:* Start hacking:

    $ vagrant up
    $ vagrant ssh

GCC Options
-----------

When compiling, the following options are recommended:

    -fno-stack-protector           # disables stack-smashing protection
    -z execstack                   # enables executable stack
    -mpreferred-stack-boundary=2   # aligns memory allocation to 2^2 bytes
    -m32                           # compile as 32-bitx86 elf file

Since the `-mpreferred-stack-boundary=2` option affects how the machine
allocates memory on the stack, it also affects the displacement calculation
when preparing format string exploits. Therefore, disabling this option is
recommended when practicing with format string bugs.
