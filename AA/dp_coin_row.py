import re


def solve(l: list):
    dp = [0] * len(l)

    for i in range(len(l)):
        if i - 1 >= 0:
            if i - 2 >= 0:
                dp[i] = max(dp[i - 2] + l[i], dp[i - 1])
            else:
                dp[i] = max(l[i], dp[i - 1])
        else:
            dp[i] = l[i]

    return dp


if __name__ == "__main__":
    in_str = input('Enter a list of number\n'
                   'format: 1, 2, 3\n'
                   'enter: ')
    print(solve(list(map(int, re.findall(r'\d+|-\d+', in_str)))))
