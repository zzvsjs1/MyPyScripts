while True:
    s = input('Enter: ')
    temp = []
    for i in s:
        temp.append(f'{ord(i):02x} ')
    print(''.join(temp))
    print(''.join(temp).replace(' ', ''))

