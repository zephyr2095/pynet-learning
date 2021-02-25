#!/usr/bin/env python3

'''
Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston data center routers, and it should have over ten RFC1918 IP addresses 
in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight RFC1918 IP addresses (including some addresses that
 overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight RFC1918 IP addresses. The Chicago IP addresses should 
have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
'''

houston = ['192.168.1.1', '172.30.254.1', '10.140.100.1', '172.25.25.100', '10.10.10.1', '10.1.100.1',
           '192.168.243.100', '192.168.250.250', '10.10.100.100', '10.1.1.1', '172.20.21.240', '172.63.63.117']

atlanta = ['10.1.100.1', '172.48.1.254', '192.168.212.1', '10.140.100.1',
           '172.63.56.1', '172.20.21.240', '192.168.243.100', '172.78.78.1', '192.168.250.250']

chicago = ['192.168.1.1', '172.48.1.254', '172.21.21.100', '192.168.200.200',
           '10.140.100.1', '10.10.100.100', '172.63.240.63', '192.168.250.250']


houston_set = set(houston)
atlanta_set = set(atlanta)
chicago_set = set(chicago)

# dup_houst_atlanta = houston_set & atlanta_set
dup_houst_atlanta = houston_set.intersection(atlanta_set)

print()
print('IP addresses duplicated between Houston and Atlanda DCs')
print('-' * 60)
print(dup_houst_atlanta)

dup_all_three = houston_set.intersection(atlanta_set, chicago_set)

print()
print('IP addresses duplicated between Houston, Atlanta and Chicago DCs')
print('-' * 60)
print(dup_all_three)

only_chicago = chicago_set.difference(atlanta_set, houston_set)

print()
print('IP addresses addresses only in Chicago DC')
print('-' * 60)
print(only_chicago)
print()
