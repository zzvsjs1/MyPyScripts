# MIT 6.006 Introduction to Algorithms, Spring 2020
# see: https://www.youtube.com/watch?v=r4-cftqTcdI&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=42

from bisect import bisect_left


def solve_suffix(string: str):
    dp = [1] * len(string)
    sub_strings = [[char] for char in string]
    max_lis_start_index = 0

    for i in reversed(range(len(string))):
        max_j = -1

        for j in range(i + 1, len(string)):
            if string[i] < string[j] and dp[j] + 1 > dp[i]:
                max_j = j
                dp[i] = dp[j] + 1

        if max_j != -1:
            sub_strings[i].extend(sub_strings[max_j])

            if dp[i] > dp[max_lis_start_index]:
                max_lis_start_index = i

    print(dp[max_lis_start_index])
    print(''.join(sub_strings[max_lis_start_index]))


def solve_prefix(something: []) -> int:
    dp = [1] * len(something)
    for i in range(len(dp)):
        for j in range(i):
            if something[j] < something[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)


def greedy_LIS_len(data) -> int:
    ret = []
    for each in data:
        if len(ret) == 0 or ret[-1] < each:
            ret.append(each)
        else:
            ret[bisect_left(ret, each)] = each

    return len(ret)


if __name__ == '__main__':
    my_string = 'CARBOHYDRATE'
    solve_suffix("empathy")
    print(solve_prefix(my_string))
    print(greedy_LIS_len("empathy"))
