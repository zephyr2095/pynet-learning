#!/usr/bin/env python3

'''
1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. 
Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. 
Also print out the type of the variable (you should have a list at this point).
'''

# open file
f = open('../show_version.txt')
output = f.read()

# print file contents
print(output)
print('\n')
print('Type is: ', type(output))
print('\n')

f.close()

# open file using context manager
with open('show_version.txt') as f:
    output1 = f.readlines()

print(output1)
print('\n')
print('Type is ', type(output1))
print('\n')
