def string_to_hex(string):
    hex_string = ""
    for char in string:
        hex_string += hex(ord(char))[2:].zfill(2)
    return hex_string


while True:
    ui = input('Enter: ')
    ret = string_to_hex(ui)
    for i in range(0, len(ret), 2):
        print(f'{ret[i]}{ret[i+1]} ', end='')

    print()
    print(ret)
    print()
gi