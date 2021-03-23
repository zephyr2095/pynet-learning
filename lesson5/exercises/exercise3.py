#!/usr/bin/env python3

'''
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
'''

import re


def format_mac_addr(mac_address):
    mac_address = mac_address.upper()

    if ':' in mac_address or '-' in mac_address:
        new_mac = []
        octets = re.split(r'[-:]', mac_address)

        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif '.' in mac_address:
        new_mac = []
        sections = mac_address.split('.')
        if len(sections) != 3:
            raise ValueError('ERROR!')

        for word in sections:
            if len(word) < 4:
                word = word.zfill(4)
            new_mac.append(word[:2])
            new_mac.append(word[2:])

    return ':'.join(new_mac)


# Assert tests
assert "01:23:02:34:04:56" == format_mac_addr("123.234.456")
assert "AA:BB:CC:DD:EE:FF" == format_mac_addr("aabb.ccdd.eeff")
assert "0A:0B:0C:0D:0E:0F" == format_mac_addr("a:b:c:d:e:f")
assert "01:02:0A:0B:03:44" == format_mac_addr("1:2:a:b:3:44")
assert "0A:0B:0C:0D:0E:0F" == format_mac_addr("a-b-c-d-e-f")
assert "01:02:0A:0B:03:44" == format_mac_addr("1-2-a-b-3-44")
print("Tests passed")
