import re


class ValuePair:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'({self.weight} : {self.value})'


def solve2(w_and_v: [ValuePair], n: int):
    dp = [[0 for _ in range(n + 1)] for _ in range(len(w_and_v) + 1)]

    for i in range(1, len(w_and_v) + 1):
        for j in range(1, n + 1):
            if j - w_and_v[i - 1].weight >= 0:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - w_and_v[i - 1].weight] + w_and_v[i - 1].value
                )
            else:
                dp[i][j] = dp[i - 1][j]

    return dp


def back_track(dp, w: list[ValuePair], i: int, j: int):
    if i == 0 and j == 0:
        return



    print(w[i])
    back_track(dp, w, i - 1, j - 1)
    back_track(dp, w, i - 1, j - w[i].weight)


# (3, 25) (2, 20) (1, 15), (4, 40) (5, 50) n = 6
#
# Get:
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 25, 25, 25, 25]
# [0, 0, 20, 25, 25, 45, 45]
# [0, 15, 20, 35, 40, 45, 60]
# [0, 15, 20, 35, 40, 55, 60]
# [0, 15, 20, 35, 40, 55, 65]
if __name__ == '__main__':
    temp: [(int, int)] = [ValuePair(int(d1), int(d2))
                          for d1, d2 in
                          re.findall(r'\((\d+), (\d+)\)',
                                     input('Enter pair of (weight, value): '))]

    dp = solve2(temp, int(input('Enter n: ')))

    for i in dp:
        print(i)

    print()
    print(f'Answer {dp[-1][-1]}')

    #back_track(dp, temp, len(dp) - 1, len(dp[-1]) - 1)