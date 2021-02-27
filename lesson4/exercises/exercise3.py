#!/usr/bin/env python3

'''
Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version, serial number, and configuration register values.

Your output should look as follows:
OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
'''

import re

with open('show_version.txt') as f:
    data = f.read()

os_version = re.search(r'^Cisco .*, Version (.*),', data).group(1)
serial_number = re.search(r'^Processor board ID (.*$)',
                          data, flags=re.M).group(1)
config_register = re.search(
    r'^Configuration register is (.*$)', data, flags=re.M).group(1)

print()
print(f'OS Version: {os_version}')
print(f'Serial Number: {serial_number}')
print(f'Config Register: {config_register}')
print()
