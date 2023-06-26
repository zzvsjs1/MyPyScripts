key = input('Enter your full name and student ID: ')
plant_text = input('Enter your RMIT student email address: ')

key = [hex(ord(i)).replace('0x', '') for i in key]
plant_text = [hex(ord(i)).replace('0x', '') for i in plant_text][:16]

print('Key 128 bit hex')

for i in key:
    print(i, end=' ')
print()
for i in key:
    print(chr(int(i, 16)), end=' ')

print()

print('Plant text 128 bit hex')
for i in plant_text:
    print(i, end=' ')
print()
for i in plant_text:
    print(chr(int(i, 16)), end=' ')

