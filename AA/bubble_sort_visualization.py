import re

COMPARE = 0
SWAP = 0


def do_bubble_sort(in_list: list):
    global COMPARE
    global SWAP

    if len(in_list) < 2:
        return

    print(f'Original: {in_list}')

    last = len(in_list)
    while last > 0:
        i = 0
        j = 1
        while j < last:
            if in_list[i] > in_list[j]:
                in_list[i], in_list[j] = in_list[j], in_list[i]
                SWAP += 1

            COMPARE += 1

            i += 1
            j += 1

        print(f'Step {len(in_list) - last + 1}: {in_list}')
        last -= 1


def bubble_s(in_l: []):
    global COMPARE
    global SWAP

    step = 0
    n = len(in_l)
    for i in range(n - 1):
        for j in range(n - 2 - i + 1):
            COMPARE += 1
            if in_l[j + 1] < in_l[j]:
                in_l[j], in_l[j + 1] = in_l[j + 1], in_l[j]
                SWAP += 1

        print(f'Round {step + 1}: {in_l} ', end='')
        print(f'compare: {COMPARE} swap: {SWAP}')
        step += 1


def bubble_so(in_l: []):
    global COMPARE
    global SWAP

    step = 0
    n = len(in_l)
    for i in range(n - 1):
        is_exchanges = False
        for j in range(n - 2 - i + 1):
            COMPARE += 1
            if in_l[j + 1] < in_l[j]:
                is_exchanges = True
                in_l[j], in_l[j + 1] = in_l[j + 1], in_l[j]
                SWAP += 1

        print(f'Round {step + 1}: {in_l} ', end='')
        print(f'compare: {COMPARE} swap: {SWAP}')
        step += 1

        if not is_exchanges:
            return


def do_opt_bubble_sort(in_list: list):
    global COMPARE
    global SWAP

    is_swap: bool = False

    for i in range(len(in_list) - 1):
        print(f'Turn {i}: {in_list}')
        for j in range(len(in_list) - 1 - i):
            if in_list[j + 1] < in_list[j]:
                in_list[j + 1], in_list[j] = in_list[j], in_list[j + 1]
                is_swap = True
                SWAP += 1
            COMPARE += 1

        if not is_swap:
            return

        is_swap = False


if __name__ == "__main__":
    in_str = input('Enter data\n'
                   'Split by comma or space\n'
                   'enter: ')

    m = [tu for tu in re.findall(r'(-?\w+) *', in_str)]
    ty = input('Data type: ')
    exec(f'm = list(map({ty}, m))')

    if input('\nEarly-Termination (y or n)? ').lower() == 'y':
        print()
        bubble_so(m)
    else:
        print()
        bubble_s(m)

    print(f'compare: {COMPARE}')
    print(f'swap: {SWAP}')
