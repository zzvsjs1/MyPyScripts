from random import Random

RANDOM = Random()


def qsort(in_list: list, left: int, right: int):
    if left < right:
        q = random_partition(in_list, left, right)
        qsort(in_list, left, q - 1)
        qsort(in_list, q + 1, right)

def select(l: list, left: int, right: int, n: int):
    while True:
        if left == right:
            return l[left]

        pivot = random_partition(l, left, right)
        if n == pivot:
            return l[n]

        if n < pivot:
            right = pivot - 1
        else:
            left = pivot + 1


def random_partition(in_list: list, left: int, right: int) -> int:
    index = RANDOM.randint(left, right)
    in_list[index], in_list[left] = in_list[left], in_list[index]
    return partition(in_list, left, right)


def partition(in_list: list, left: int, right: int) -> int:
    pivot = left
    for j in range(pivot + 1, right + 1):
        if in_list[j] < in_list[left]:
            pivot += 1
            in_list[pivot], in_list[j] = in_list[j], in_list[pivot]

    in_list[pivot], in_list[left] = in_list[left], in_list[pivot]
    return pivot


if __name__ == '__main__':
    value = [100, 21, 3, 8, 9, 60, 2, 7]
    print(select(value, 0, len(value) - 1, 1))
    print(select(value, 0, len(value) - 1, 1))
    print(select(value, 0, len(value) - 1, 2))
