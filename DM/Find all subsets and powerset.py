import itertools


def print_t(t: tuple):
    if len(subset) == 0:
        print('∅')
        return

    for i, j in enumerate(t):
        if i != len(t) - 1:
            print(f'{j}, ', end='')
        else:
            print(f'{j}', end='\n')


while True:
    user_in = input('Enter: ').replace(' ', '').split(',')
    subsets = []
    for i in range(len(user_in) + 1):
        subsets.extend(list(itertools.combinations(user_in, i)))

    print(f'\nThere {len(subsets)} subsets.')
    for subset in subsets:
        print_t(subset)
    print()
