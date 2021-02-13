#!/usr/bin/env python3

from __future__ import print_function


'''
4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
'''

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

# Remove leading and trailing whitespace
show_version = show_version.strip()

# Split string into list
fields = show_version.split()
model = fields[1]
serial_number = fields[2]

print("\n")
vendor_cisco = "cisco" in model.lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))

model_881 = "881" in model
print("Checking if model contains 881: {}".format(model_881))

print("Serial number: {}".format(serial_number))
print("\n")
