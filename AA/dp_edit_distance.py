def solve(word1: str, word2: str) -> list[list[int]]:
    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for i in range(len(dp[0])):
        dp[0][i] = i

    for i, d in zip(range(len(dp)), dp):
        d[0] = i

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1],
                )

    return dp


if __name__ == "__main__":
    string = input('Enter X Y, split by space: ').split()
    ans = solve(string[0], string[1])
    for i in ans:
        print(i)

    print(f'\nAnswer: {ans[-1][-1]}')
