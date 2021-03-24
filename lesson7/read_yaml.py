#!/usr/bin/env python3

import yaml
from pprint import pprint

filename = 'my_devices.yml'
with open(filename) as f:
    output = yaml.load(f, Loader=yaml.FullLoader)

pprint(output)

# print(output['rtr2'])
# print(output['rtr4'])
