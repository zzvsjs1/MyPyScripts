import re

if __name__ == '__main__':
    a = re.compile(r'(\d+)/(\d+)')
    while True:
        user_input = input('Expression: ')
        p = a.match(user_input.replace(' ', ''))
        if p is not None:
            print(divmod(int(p.group(1)), int(p.group(2))))
