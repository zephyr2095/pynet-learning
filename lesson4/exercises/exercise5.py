#!/usr/bin/env python3

'''
Read the 'show_ipv6_intf.txt' file.

From this file, use Python regular expressions to extract the two IPv6 addresses.

The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of the literal characters in the IPv6 address.

From this, create a list of IPv6 addresses that includes only the above two addresses.

Print this list to the screen.
'''

import re

with open('show_ipv6_intf.txt') as f:
    show_ipv6_intf = f.read()

ipv6_list = []
ipv6_list = re.findall(r'\d+:.*/.{2}', show_ipv6_intf, flags=re.M)

print()
print(ipv6_list)
print()
