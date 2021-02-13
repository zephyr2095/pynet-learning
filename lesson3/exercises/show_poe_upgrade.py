#!/usr/bin/env python3

'''
Parse show poe controller output from Juniper devices and see which units need poe firmware update.

Units needing an update have '**' in front of them'
'''

with open('show_poe_controller.txt') as f:
    output = f.readlines()

found = False
print('Units needing firmware update')
print('-' * 30)
for line in output:
    if line.startswith('   '):
        fields = line.split()
        if '**' in fields[0] and '**New' not in fields[0]:
            unit_id = fields[0]
            found = True
            print(f'Unit: {unit_id}')
if found == False:
    print('No units need upgrades...')
print()
