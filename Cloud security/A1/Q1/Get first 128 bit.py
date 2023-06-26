name = input()
# Get hex number.
b = [hex(ord(i)).replace('0x', '') for i in name]

for i in b[:16]:
    print(i, end=' ')
print()
for i in b[:16]:
    print(chr(int(i, 16)), end=' ')


a = '73 33 36 34 31 37 30 35 40 73 74 75 64 65 6e 74'.replace(' ', '')

for i, j in enumerate(a):
    print(f'{S_BOX[int(j, 16)]:x}', end=' ' if i != 0 and i & 1 != 0 else '')
print()
