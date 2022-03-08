def merge_sort(ilist: list):
    if len(ilist) > 1:
        b = ilist[:len(ilist) // 2 - 1]
        c = ilist[len(ilist) // 2:]
        merge_sort(b)
        merge_sort(c)
        merge(b, c, ilist)


def merge(a: list, b: list, to: list):
    i = 0
    j = 0
    l = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            to[l] = a[i]
            i += 1
        else:
            to[l] = b[j]
            j += 1
        l += 1

    if i != len(a):
        for k in range(i, len(a)):
            to[l] = a[k]
            l += 1

    if j != len(a):
        for k in range(j, len(b)):
            to[l] = a[k]
            l += 1


if __name__ == '__main__':
    li = list(reversed(range(10)))
    merge_sort(li)
    print(li)