def solve(ilist: [int], t: int) -> bool:
    return solve_sub(ilist, 0, t) \
        if t != 0 \
        else \
        (True if 0 in ilist else False)


def solve_sub(ilist: [int], i: int, t: int) -> bool:
    if t == 0:
        return True

    if i == len(ilist):
        return False

    temp = solve_sub(ilist, i + 1, t)
    if ilist[i] <= t:
        return temp or solve_sub(ilist, i + 1, t - ilist[i])

    return temp


if __name__ == '__main__':
    print(solve([1, 2, 3, 4], 8))
