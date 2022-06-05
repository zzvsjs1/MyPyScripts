def solve(height: int, width: int):
    dp = []
    for i in range(height):
        dp.append([0] * width)
    for i in range(height):
        dp[i][0] = 1
    for i in range(1, width):
        dp[0][i] = 1

    solve_r(dp, height - 1, width - 1)
    return dp


def solve_r(dp: list[list], i: int, j: int):
    if i == 0 or j == 0:
        return 1

    dp[i][j] = solve_r(dp, i, j - 1) + solve_r(dp, i - 1, j)
    return dp[i][j]


def transfer(dp: list[list]):
    size = len(dp)
    for i in range(size // 2):
        for j in range(1, size):
            dp[i][j], dp[-1 - i][j] = dp[-1 - i][j], dp[i][j]


if __name__ == '__main__':
    s = int(input('Enter size (e.g 5): '))
    res = solve(s, s)
    for o in res:
        print(o)

    print('\nTransfer from left lower to right upper', end='\n\n')

    transfer(res)
    for o in res:
        print(o)

