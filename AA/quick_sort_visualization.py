import re

counter: int = 0


def print_partition(in_list: list, l: int, r: int) -> str:
    list_str = ['[']
    for i in range(l):
        list_str.append(f'{str(in_list[i])}, ')

    list_str.append('[')
    for i in range(l, r):
        list_str.append(f'{in_list[i]}, ')

    list_str.append(f'{in_list[r]}]')

    if len(in_list) - 1 != r:
        list_str.append(', ')

    i_max = len(in_list) - 1
    i = r + 1
    while i <= i_max:
        list_str.append(str(in_list[i]))
        if i == i_max:
            break
        list_str.append(', ')
        i += 1

    list_str.append(']')
    return ''.join(list_str)


def do_quick_sort(in_list: list, l: int, r: int):
    if l < r:
        pivot = qsort_impl(in_list, l, r)
        do_quick_sort(in_list, l, pivot - 1)
        do_quick_sort(in_list, pivot + 1, r)


def qsort_impl(in_list: list, l: int, r: int) -> int:
    global counter
    p = in_list[l]
    i = l
    j = r + 1

    while True:
        while True:
            i += 1
            if in_list[i] >= p or i >= r:
                break

        while True:
            j -= 1
            if in_list[j] <= p:
                break

        in_list[i], in_list[j] = in_list[j], in_list[i]

        print(f'Step {counter}: {print_partition(in_list, l, r)}')
        counter += 1
        if i >= j:
            break

    in_list[i], in_list[j] = in_list[j], in_list[i]
    in_list[l], in_list[j] = in_list[j], in_list[l]

    print(f'Step {counter}: {print_partition(in_list, l, r)}')
    counter += 1
    return j


if __name__ == "__main__":
    in_str = input('Enter a list of number\n'
                   'format: 1, 2, 3\n'
                   'enter: ')
    m = list(map(int, re.findall(r'\d+|-\d+', in_str)))
    do_quick_sort(m, 0, len(m) - 1)
    print(f'Sorted: {m}')
