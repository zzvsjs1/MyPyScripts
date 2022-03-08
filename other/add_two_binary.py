import re

if __name__ == '__main__':
    a = re.compile(r'([1|0]+)(\+)([1|0]+)')
    while True:
        user_input = input('Expression b + b: ').replace('.', '').replace(' ', '')
        p = a.match(user_input)
        if p is not None:
            print(bin((int(p.group(1), 2) + int(p.group(3), 2))).replace('0b', ''))
