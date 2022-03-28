def solve(ilist: [(int, int)], n):
    temp = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(1, i + 1):
            temp[i] = max(temp[i - j] + ilist[j - 1][1], temp[i])

    print(temp)


if __name__ == '__main__':
    solve([(1, 1), (2, 10), (3, 13), (4, 18), (5, 20), (6, 31), (7, 32)], 7)
