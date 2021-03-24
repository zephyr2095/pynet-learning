#!/usr/bin/env python3

import yaml

my_dict = {
    'rtr1': {
        'ip_addr': '10.1.1.1',
        'username': 'admin',
        'password': 'whatever',
        'bgp_peers': ['10.100.1.1', '10.100.1.2', '10.100.1.3', '10.100.1.4']
    },
    'rtr2': {
        'ip_addr': '10.1.1.22',
        'username': 'admin2',
        'password': 'cisco1234',
        'bgp_peers': ['192.168.1.22', '2.2.2.2']
    }
}

filename = 'output.yml'
with open(filename, 'w') as f:
    output = yaml.dump(my_dict, f, default_flow_style=False)
