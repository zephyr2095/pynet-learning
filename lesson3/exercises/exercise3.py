#!/usr/bin/env python3

'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered 
the remote "System Name" and remote "Port id". Save these two items into variables and print them to the screen. You should extract
only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). 
Break out of your loop once you have retrieved these two items.
'''

# Open file using with open method
with open('show_lldp_neighbors_detail.txt') as f:
    output = f.readlines()

# Set flag variables to false
found1, found2 = (False, False)
for line in output:
    # Split string on ':' character
    fields = line.split(':')
    # Check for Port id and System name then assign value to variable and print
    if 'Port id' in fields[0]:
        port_id = fields[1].strip()
        print(port_id)
        found1 = True
    elif 'System Name' in fields[0]:
        system_name = fields[1].strip()
        print(system_name)
        found2 = True

    # If flags are true break from loop
    if found1 and found2 == True:
        print('breaking...')
        break
