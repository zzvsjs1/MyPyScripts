import re
from rich.console import Console

COUNTER: int = 0
TURN: int = 0
COMPARES = 0
SWAP = 0
console = Console()


def pri(ilist: list, pivot: int):
    copy = ilist[:pivot]
    copy2 = ilist[pivot + 1:]

    s = '['

    if len(copy) != 0:
        s += f'{str(copy)}, '

    s += f'[{ilist[pivot]}]'

    if pivot != len(ilist) - 1:
        s += ', '

    if len(copy2) != 0:
        s += str(copy2)

    return s + ']'


def do_quick_sort(in_list: list, left: int, right: int):
    global COMPARES
    COMPARES += 1
    if left < right:
        pivot = qsort_impl(in_list, left, right)
        do_quick_sort(in_list, left, pivot - 1)
        do_quick_sort(in_list, pivot + 1, right)


def qsort_impl(in_list: list, left: int, right: int) -> int:
    global COUNTER, COMPARES, SWAP, TURN

    p = in_list[left]
    i = left
    j = right + 1

    while True:
        while True:
            i += 1
            COMPARES += 1
            if in_list[i] >= p or i >= right:
                break

        while True:
            j -= 1
            COMPARES += 1
            if in_list[j] <= p:
                break

        SWAP += 1
        in_list[i], in_list[j] = in_list[j], in_list[i]

        print(f'Step {COUNTER}: {in_list} Compare: {COMPARES} Swap: {SWAP}')
        COUNTER += 1

        COMPARES += 1

        if i >= j:
            break

    SWAP += 2
    in_list[i], in_list[j] = in_list[j], in_list[i]
    in_list[left], in_list[j] = in_list[j], in_list[left]

    TURN += 1
    console.print(f'Step {COUNTER}: {pri(in_list, j)} Range: {left} - {right}  '
                  f'Turn: {TURN} Pivot: {in_list[j]} in index {j} '
                  f'Compare: {COMPARES} Swap: {SWAP}', style='red')
    # console.print(f'Verify {in_list}', style='red')
    COUNTER += 1
    return j


if __name__ == "__main__":
    # 15 21 1 25 12 6 8 3 5 19 10 18
    # 42 30 9 40 4 29 35 40 15 43 45 13
    in_str = input('Enter data\n'
                   'Split by comma or space\n'
                   'enter: ')

    m = [tu for tu in re.findall(r'(-?\w+) *', in_str)]
    ty = input('Data type: ')
    exec(f'm = list(map({ty}, m))')

    do_quick_sort(m, 0, len(m) - 1)
    console.print(f'\nSorted: {m}', end='\n\n', style='red')
    console.print(f'Total Swap {SWAP} Compare {COMPARES}', style='blue')
