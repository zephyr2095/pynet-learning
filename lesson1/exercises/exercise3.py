#!/usr/bin/env python3

from __future__ import print_function, unicode_literals

'''
3.   Create three different variables the first variable should use all lower case characters with underscore ( _ )
as the word separator. The second variable should use all upper case characters with underscore as the word
separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python
 variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''

first_variable = "fe80::0"
SECOND_VAR = "2001:db8::"
var_3 = "ff00::100"

print("Variable 1 equals Variable 2: ")
print(first_variable == SECOND_VAR)
print("Variable 1 is not equal to Variable 3: ")
print(first_variable != var_3)
