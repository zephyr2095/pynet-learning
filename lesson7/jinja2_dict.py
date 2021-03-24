#!/usr/bin/env python3

import jinja2

bgp_vars = {
    'routers': {
        'sf_rtr1': '10.10.10.1',
        'sf_rtr2': '10.10.10.2',
        'la_rtr1': '10.100.18.1',
        'denver_rtr1': '172.30.100.1',
    },
    'ip_list': [
        '192.168.1.100',
        '172.63.63.1',
        '10.254.200.200'
    ],
}

z_template = '''

{%- for router_name, ip_addr in routers.items() %}
{{ router_name }} >>> {{ ip_addr }}
{%- endfor %}

{%- for ip_addr in ip_list %}
{{ ip_addr }}
{%- endfor %}
'''

# Nested for loops in template
nested_template = '''

{%- for router_name, ip_addr in routers.items() %}
{{ router_name }} >>> {{ ip_addr }}
    {%- for ip_addr in ip_list %}
    {{ ip_addr }}
    {%- endfor %}
{%- endfor %}
'''

# Can reference dictionary keys directly
ref_template = '''
    {{ routers['sf_rtr1'] }}
    {{ routers.denver_rtr1 }}
'''

template = jinja2.Template(z_template)
print(template.render(bgp_vars))

template2 = jinja2.Template(nested_template)
print(template2.render(bgp_vars))

template3 = jinja2.Template(ref_template)
print(template3.render(bgp_vars))
