import re


class WVPair:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'({self.weight} : {self.value})'


def solve(w_and_v: [WVPair], n: int):
    dp = [[0 for _ in range(n + 1)] for _ in range(len(w_and_v) + 1)]

    for i in range(1, len(w_and_v) + 1):
        for w in range(1, n + 1):
            if w - w_and_v[i - 1].weight >= 0:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - w_and_v[i - 1].weight] + w_and_v[i - 1].value
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp


def top_down(w_and_v: list[WVPair], n: int):
    dp = [[-1 for _ in range(n + 1)] for _ in range(len(w_and_v) + 1)]

    for i in range(len(dp[0])):
        dp[0][i] = 0

    for i in range(1, len(dp)):
        dp[i][0] = 0

    top_down_r(dp, len(w_and_v), n, w_and_v)
    return dp


def top_down_r(dp: list[list], i: int, w: int, w_and_v: list[WVPair]):
    if dp[i][w] < 0:
        if w < w_and_v[i - 1].weight:
            x = top_down_r(
                dp,
                i - 1,
                w,
                w_and_v
            )
        else:
            x = max(
                top_down_r(dp, i - 1, w, w_and_v),
                w_and_v[i - 1].value + top_down_r(
                    dp,
                    i - 1,
                    w - w_and_v[i - 1].weight,
                    w_and_v
                )
            )

        dp[i][w] = x

    return dp[i][w]


# (3, 25) (2, 20) (1, 15), (4, 40) (5, 50) n = 6
#
# Get:
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 25, 25, 25, 25]
# [0, 0, 20, 25, 25, 45, 45]
# [0, 15, 20, 35, 40, 45, 60]
# [0, 15, 20, 35, 40, 55, 60]
# [0, 15, 20, 35, 40, 55, 65]
#
# Top-down:
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 25, 25, 25, 25]
# [0, 0, 20, -, -, 45, 45]
# [0, 15, 20, -, -, -, 60]
# [0, 15, -, -, -, -, 60]
# [0, -, -, -, -, -, 65]
if __name__ == '__main__':
    temp: [(int, int)] = [WVPair(int(d1), int(d2))
                          for d1, d2 in
                          re.findall(r'\((\d+), *(\d+)\)',
                                     input('Enter pair of (weight, value): '))]

    match input('Is (value, weight)? ').lower():
        case 'y' | 'true' | '1':
            for each in temp:
                mi = each.weight
                each.weight = each.value
                each.value = mi

    n = int(input('Enter n|m whatever: '))

    match input('Is top down? ').lower():
        case 'y' | 'true' | '1':
            dp = top_down(temp, n)
        case _:
            dp = solve(temp, n)

    for i in dp:
        print(str(i).replace('-1', '-'))

    print()
    print(f'Answer {dp[-1][-1]}')
