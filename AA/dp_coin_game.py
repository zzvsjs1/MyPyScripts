from enum import Enum


class MyType(Enum):
    YOU = 0
    ME = 1


def solve(v: list):
    return solve_recursive(v, 0, len(v) - 1, MyType.ME)


def solve_recursive(v: list, i, j, you_me: MyType):
    if i == j:
        return v[i] if you_me == MyType.ME else 0

    return max(solve_recursive(v, i + 1, j, MyType.YOU) + v[i], solve_recursive(v, i, j - 1, MyType.YOU) + v[j]) \
        if you_me == MyType.ME \
        else \
        min(solve_recursive(v, i + 1, j, MyType.ME), solve_recursive(v, i, j - 1, MyType.ME))


if __name__ == '__main__':
    coins = [5, 10, 100, 25]
    print(solve(coins))