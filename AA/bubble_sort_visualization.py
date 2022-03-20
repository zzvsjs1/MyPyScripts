import re


def do_bubble_sort(in_list: list):
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

            i += 1
            j += 1

        print(f'Step {len(in_list) - last + 1}: {in_list}')
        last -= 1


def do_opt_bubble_sort(in_list: list):
    is_swap: bool = False

    # To last - 1
    for i in range(len(in_list) - 1):
        print(f'Turn {i}: {in_list}')
        for j in range(len(in_list) - 1 - i):
            if in_list[j + 1] < in_list[j]:
                in_list[j + 1], in_list[j] = in_list[j], in_list[j + 1]
                is_swap = True

        if not is_swap:
            return

        is_swap = False


if __name__ == "__main__":
    in_str = input('Enter a list of number\n'
                   'format: 1, 2, 3\n'
                   'enter: ')
    m = list(map(int, re.findall(r'\d+|-\d+', in_str)))
    do_opt_bubble_sort(m)
