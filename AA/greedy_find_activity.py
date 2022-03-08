def start_find(s: list[int], f: list[int]):
    n: int = len(s)
    a: list[tuple[int, int]] = [(s[0], f[0])]
    k: int = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            a.append((s[m], f[m]))
            k = m

    return a


ss: list[int] = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
ff: list[int] = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
print(start_find(ss, ff))
