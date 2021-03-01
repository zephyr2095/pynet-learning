#!/usr/bin/env python3

"""
Using a named regular expression (?P<name>), extract the model from the below string:
show_version = '''

Cisco 881 (MPC8300) processor(revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network(VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash(Read/Write)
'''
Note that, in this example, '881' is the relevant model. Your regular expression should not, however, include '881' in its search pattern 
since this number changes across devices.

Using a named regular expression, also extract the '236544K/25600K' memory string.

Once again, none of the actual digits of the memory on this device should be used in the regular expression search pattern.

Print both the model number and the memory string to the screen.
"""

import re

show_version = '''

Cisco 881 (MPC8300) processor(revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network(VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash(Read/Write)
'''

device_info = {}
device_info.update(re.search(r'^Cisco (?P<name>.*?) ',
                             show_version, flags=re.M).groupdict(1))
device_info.update(re.search(r'^Cisco .* with (?P<memory>.*?) ',
                             show_version, flags=re.M).groupdict(1))

print()
print(f"Model number: {device_info['name']}")
print(f"Memory: {device_info['memory']}")
print()


# Alternate method - from Kirk Byers' Github answers for lesson exercises
#
# match = re.search(
#    r"^Cisco (?P<model>\S+).* with (?P<memory>\S+) bytes of memory",
#    show_version,
#    flags=re.M,
# )
# model = match.groupdict()["model"]
# memory = match.groupdict()["memory"]
