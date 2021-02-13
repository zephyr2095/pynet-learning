#!/usr/bin/env python3

'''
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

# Create list with 5 IP addresses
ip_list = ['192.168.1.1', '10.100.1.250', '172.16.24.50', '8.8.8.8']

# Add two IP addresses via .append() method
ip_list.append('10.1.1.1')
ip_list.append('172.1.1.1')

# Add two more IP addresses via .extend() method
two_more = ['172.63.63.117', '10.148.250.1']
ip_list.extend(two_more)

# Add two more via list concatenation
ip_list = ip_list + ['4.4.4.4', '9.9.9.9']

print(f'Entire IP list : {ip_list}')
print(f'First IP address: {ip_list[0]}')
x = len(ip_list)
print(f'Last IP address: {ip_list[x - 1]}')

'''
Can use ip_list[-1] to get last position in list

print(ip_list[-1])
'''

# Pop first IP address off list
ip_list.pop(0)
# Pop last IP address off list
ip_list.pop()

# Replace first IP with '2.2.2.2' and print out new first IP
ip_list[0] = '2.2.2.2'
print(ip_list[0])
