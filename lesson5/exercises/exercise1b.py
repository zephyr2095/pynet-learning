#!/usr/bin/env python3

'''
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. 
Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
'''


def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print('IP address is: {}'.format(ip_addr))
    print('Username is: {}'.format(username))
    print('Password is: {}'.format(password))
    print('Device Type is: {}'.format(device_type))
    print()


# Call ssh_conn2 function with and without specifying device_type
ssh_conn2('192.168.1.1', 'cisco', 'admin123', 'cisco_nxos')
ssh_conn2('172.63.17.1', 'admin', 'cisco')

device_info = {
    'ip_addr': '10.10.10.1',
    'password': 'cisco12345',
    'username': 'admin2',
    'device_type': 'cisco_xr'
}

# Call ssh_con2 using **kwargs
ssh_conn2(**device_info)
