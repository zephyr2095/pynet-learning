#!/usr/bin/env python3

import jinja2

# Initial bgp_vars
'''
bgp_vars = {
    "local_as": 10,
    "peer1_ip": "10.255.255.2",
    "peer1_as": 20,
    "route_1": "10.10.200.0/24",
    "route_2": "10.10.201.0/24",
    "route_3": "10.10.202.0/24",
}
'''
# New bgp_vars using list for advertised_routes key value pair
advertised_routes = ['10.10.200.0/24', '10.10.201.0/24', '10.10.202.0/24']
bgp_vars = {
    "local_as": 10,
    "peer1_ip": "10.255.255.2",
    "peer1_as": 20,
    "advertised_routes": advertised_routes,
}

template_file = 'nxos_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

template = jinja2.Template(bgp_template)
print(template.render(bgp_vars))
