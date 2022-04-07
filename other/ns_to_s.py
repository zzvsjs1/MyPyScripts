from decimal import Decimal


ns = Decimal(input('ns: '))
ms = ns / 1000000
s = ns / 1000000000
minutes = ns / (1000000000 * 60)
hours = ns / (1000000000 * 60 * 60)
print(f'Ms: {ms}')
print(f'S: {s}')
print(f'Min: {minutes}')
print(f'Hours: {hours}')