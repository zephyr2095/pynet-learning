#!/usr/bin/env python3

'''
Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
'''

network_device = {'ip_addr': '192.168.1.1',
                  'vendor': 'cisco', 'username': 'admin', 'password': 'cisco'}

print(f"IP address: {network_device['ip_addr']}")

if network_device['vendor'] == 'cisco':
    network_device['platform'] = 'ios'
elif network_device['vendor'] == 'juniper':
    network_device['platform'] = 'junos'

bgp_fields = {'bgp_as': '65000', 'peer_as': '65100', 'peer_ip': '172.30.16.1'}

network_device.update(bgp_fields)

print()
print('network_device dictionary keys')
print()
for keys in network_device.keys():
    print(keys)

print()
print('network_device dictionary keys and values')
print()
for k, v in network_device.items():
    print(k)
    print(v)
    print('-' * 30)
