def solve(x: int | float, n: int) -> int | float:
    if n == 0:
        return 1

    if n == 1:
        return x

    if n & 1:
        temp = solve(x, (n - 1) // 2)
        return temp * temp * x

    temp = solve(x, n // 2)
    return temp * temp


if __name__ == '__main__':
    print(solve(9.5, 7))
