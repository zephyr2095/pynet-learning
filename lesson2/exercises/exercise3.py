#!/usr/bin/env python3

'''
3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string 
using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
'''

from pprint import pprint

# Open 'show_arp.txt' file and chuck it into list of each line
with open('show_arp.txt') as f:
    output = f.readlines()

# Remove header line
output = output[1:]

pprint(output)

# Sort list
output.sort()

# Create new list slice with first 3 entries
arp_entries = output[:3]

# Join list of strings back into sinlge string
arp_entries = '\n'.join(arp_entries)

# Create file containing string created above
f = open('../arp_entries.txt', 'w')
f.write(arp_entries)
f.close()
