import re


def start_dp(input_str: [(int, int)], n: int):
    dp: [int] = list(range(n + 1))
    for weight, value in input_str:
        for j in range(weight, len(dp)):
            dp[j] = max(dp[j], dp[j - weight] + value)

    print(f'Answer: {dp[n]}')


if __name__ == '__main__':
    temp: [(int, int)] = [(int(d1), int(d2)) for d1, d2 in
                          re.findall(r'\((\d+), (\d+)\)', input('Enter pair of (weight, value): '))]
    temp.sort(key=lambda w: w[0])
    start_dp(temp, int(input('Enter n: ')))
