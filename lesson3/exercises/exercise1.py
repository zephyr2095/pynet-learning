#!/usr/bin/env python3

'''
1. Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract 
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element 
in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen. 

Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''

from pprint import pprint

vlan_list = []
with open('show_vlan.txt') as f:
    output = f.readlines()

for line in output:
    # Skip lines with VLAN or '-----' or a space
    if 'VLAN' in line or '-----' in line or line.startswith(' '):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()
