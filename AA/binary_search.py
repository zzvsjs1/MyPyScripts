def binary_search_return_index(ilist: list, item) -> int:
    l = 0
    r = len(ilist) - 1
    print(ilist)
    while l <= r:
        m = (l + r) // 2
        if ilist[m] < item:
            l = m + 1
            print(ilist[l:r])
        elif ilist[m] > item:
            r = m - 1
            print(ilist[l:r])
        else:
            return m

    return -1


if __name__ == '__main__':
    print(binary_search_return_index(list(range(10)), 8))
