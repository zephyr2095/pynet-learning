#!/usr/bin/env python3

ip_addr1 = "172.16.1.1"
ip_addr2 = "172.31.17.99"
ip_addr3 = "217.88.17.1"

'''
Format method for formatting strings. Can use positional variable substitution or variable name.
Example below is position. Next example is passing named argument instead of position
'''
# Position
print("\n")
print("-" * 80)
print("{}{}{}".format(ip_addr1, ip_addr2, ip_addr3))
print("\n")

# Variable
print("\n")
print("-" * 80)
print("{my_ip}{ip}{ip_alt}".format(
    ip_alt=ip_addr1, my_ip=ip_addr2, ip=ip_addr3))
print("\n")

'''
Can add column formatting
:> is right justified
:< is left justified
:^ is centered
:20 pads columns by 20 characters
'''
print("\n")
print("-" * 80)
print("{:>20}{:>20}{:>20}".format(ip_addr1, ip_addr2, ip_addr3))
print("\n")

'''
Convert IP address to octets
Split on '.' and make a list of octects
Print list of octets
'''

ip_addr = "192.168.1.1"
octets = ip_addr.split(".")

print("\n")
print("-" * 80)
print("{:10}{:10}{:10}{:10}".format(
    octets[0], octets[1], octets[2], octets[3]))
# Can use *list_var to pass in list
print("{:10}{:10}{:10}{:10}".format(*octets))
print("-" * 80)
print("\n")

'''
f string can reference variable directly in string
'''
port1 = 80
port2 = 443
print(f"My IP address is: {ip_addr1} {port1}")
print(f"My IP address is: {ip_addr2:^20} {port2:^8}")
