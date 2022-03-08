import subprocess


def do_quick_sort(in_list: list, l: int, r: int):
    if l < r:
        pivot = qsort_impl(in_list, l, r)
        do_quick_sort(in_list, l, pivot - 1)
        do_quick_sort(in_list, pivot + 1, r)


def qsort_impl(in_list: list, l: int, r: int) -> int:
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

        print(in_list)
        if i >= j:
            break

    in_list[i], in_list[j] = in_list[j], in_list[i]
    in_list[l], in_list[j] = in_list[j], in_list[l]

    print(in_list)
    return j


if __name__ == "__main__":
    input_list = [45, 789, 456, -123, 0, 1, 2, 3]
    do_quick_sort(input_list, 0, len(input_list) - 1)
