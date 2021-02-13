#!/usr/bin/env python3

'''
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and 
last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''

from __future__ import print_function, unicode_literals

with open('show_ip_bgp_summ.txt') as f:
    output = f.readlines()

first_line = output[0]
last_line = output[-1]

first_line = first_line.split()
local_as = first_line[-1]

last_line = last_line.split()
peer_ip = last_line[0]

print(f'Local AS number: {local_as}')
print(f'Peer IP address: {peer_ip}')
