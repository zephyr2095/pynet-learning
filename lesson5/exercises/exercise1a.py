#!/usr/bin/env python3

'''
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. 
The function should print out each of these three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
'''

# Create ssh_conn function with three parameters: ip_addr, username, password


def ssh_conn(ip_addr, username, password):
    print(f'IP address is: {ip_addr}')
    print(f'Username is: {username}')
    print(f'Password is: {password}')
    print()


# Call ssh_conn using positional arguments
ssh_conn('10.1.100.1', 'admin', 'cisco')

# Call ssh_conn using named arguments
ssh_conn(password='admin123', ip_addr='192.168.1.1', username='admin')

# Call ssh_conn using mix of positional and named arguments
ssh_conn('172.32.63.56', password='cisco1234', username='local_admin')
