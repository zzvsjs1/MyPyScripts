# MIT 6.006 Introduction to Algorithms, Spring 2020
# see: https://www.youtube.com/watch?v=r4-cftqTcdI&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=42

def max_score_prefix(in_list: list):
    dp = [0] * (len(in_list) + 1)
    in_list.insert(0, 1)
    for i in range(1, len(in_list)):
        dp[i - 1] = max(dp[i - 2], dp[i - 2] + in_list[i], dp[i - 3] + in_list[i] * in_list[i - 1])

    print(dp[-2])


def max_score_suffix(in_list: list):
    dp = [0] * (len(in_list) + 2)
    in_list.append(1)
    for i in reversed(range(len(in_list) - 1)):
        dp[i] = max(dp[i + 1], dp[i + 1] + in_list[i], dp[i + 2] + in_list[i] * in_list[i + 1])

    print(dp[0])


if __name__ == '__main__':
    bowling_pins = [1, 1, 9, 9, 2, -5, -5]
    max_score_suffix(bowling_pins)
