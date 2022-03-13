def find_min(a_list: list, start: int, end: int):
    if start == end:
        return start

    i = find_min(a_list, start, (start + end) // 2)
    j = find_min(a_list, (start + end) // 2 + 1, end)
    if a_list[i] <= a_list[j]:
        return i

    return j


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
print(a)
print(find_min(a, 0, len(a) - 1))
