import itertools as it


def reverse_list(a_list: list):
    length = len(a_list)
    for i, j in it.zip_longest(range(length // 2),
                               reversed(range(length // 2 + 1 if length & 1 else length // 2, length))):
        a_list[i], a_list[j] = a_list[j], a_list[i]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_list(a)
print(a)
