while True:
    a = input('A: ')
    b = input('B: ')
    assert len(a) == len(b)
    c = eval(f'0x{a} ^ 0x{b}')
    print(f'\n{c:x}')
    print()
