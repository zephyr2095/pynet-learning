#!/usr/bin/env python3

'''
Use Jinja2 templating to render the following:
vlan 
   name 

Your template should be inside of your Python program for simplicity.

The output from processing your template should be as follows. This should be printed to stdout.
vlan 400
   name red400
'''

import jinja2

vlan_template = '''

vlan {{ vlan_id }}
   name {{ vlan_name }}

'''

vlan_vars = {
    'vlan_id': 400,
    'vlan_name': 'red400'
}

template = jinja2.Template(vlan_template)
print(template.render(vlan_vars))
