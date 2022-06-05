import re
from rich import console


COMPARE = 0


def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)


def merge(left: list, right: list, arr: list):
    global COMPARE

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        COMPARE += 1
        k += 1

    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1


if __name__ == '__main__':
    # 15 21 1 25 12 6 8 3 5 19 10 18
    c = console.Console()
    c.print('Merge sort is a stable sorting method.', style='bold red')
    in_str = input('Enter data\n'
                   'Split by comma or space\n'
                   'enter: ')

    m = [tu for tu in re.findall(r'(-?\w+) *', in_str)]
    ty = input('Data type: ')
    exec(f'm = list(map({ty}, m))')
    merge_sort(m)
    print(m)
    print(f'Compare {COMPARE}')
