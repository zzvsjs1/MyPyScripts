# while True:
#     a = input('Enter number: ')
#     print(int(a, 16))

# print(input().replace(' ', ''))

# while True:
#     a = input('Enter: ').split(' ')
#     for i in a:
#         print(int(i, 16))

import sympy

from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

print(limit(5 ** x, x, 100))
