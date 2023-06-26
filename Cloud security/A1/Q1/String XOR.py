while True:
    a = int(input('A: ').replace(' ', ''), 16)
    b = int(input('B: ').replace(' ', ''), 16)
    result = a ^ b
    print(f'a = {a:x} b = {b:x}')
    print(f'result = {result:x}')
    print()
