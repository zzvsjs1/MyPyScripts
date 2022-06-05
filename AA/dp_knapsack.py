import re


class ValuePair:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'({self.weight} : {self.value})'


def solve(w_and_v: [ValuePair], n: int):
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
                          re.findall(r'\((\d+), *(\d+)\)',
                                     input('Enter pair of (weight, value): '))]

    match input('Is (value, weight)? ').lower():
        case 'y' | 'true' | '1':
            for each in temp:
                mi = each.weight
                each.weight = each.value
                each.value = mi

    dp = solve(temp, int(input('Enter n|m whatever: ')))

    for i in dp:
        print(i)

    print()
    print(f'Answer {dp[-1][-1]}')
