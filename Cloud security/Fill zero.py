zero = 128
while True:
    string = input('Enter: ')
    while len(string) != zero:
        string += '0'
    assert len(string) == zero
    print()
    print(string, end='\n\n')
