def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


while True:
    num = int(input('Enter: '))
    ret = find_factors(num)
    print()
    print(f'There are {len(ret)}')
    for i, n in enumerate(ret):
        if i != len(ret) - 1:
            print(f'{n}, ', end='')
        else:
            print(f'{n}', end='')
    print()
