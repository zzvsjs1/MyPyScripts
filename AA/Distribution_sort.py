import re


def solve(li: list):
    f = {}
    for i in li:
        if i not in f:
            f[i] = 1
        else:
            f[i] += 1
    v = list(f.keys())
    v.sort()

    index = []

    print(f'\nFrequency: ')
    print('Value: ', end='')
    for i in v:
        print(f'{i} ', end='')
    print()
    print('Frequ: ', end='')
    for i in v:
        print(f[i], end=' ')
        index.append(f[i])
    print()

    for i in range(1, len(index)):
        index[i] += index[i - 1]

    print(f'\nStart index\n{index}')

    lii = li[:]
    lii.sort()
    print(f'\nFinal\n{lii}')


if __name__ == '__main__':
    in_str = input('Enter data\n'
                   'Split by comma or space\n'
                   'enter: ')

    m = [tu for tu in re.findall(r'(-?\w+) *', in_str)]
    ty = input('Data type: ')
    exec(f'm = list(map({ty}, m))')

    solve(m)
