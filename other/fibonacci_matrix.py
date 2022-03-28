import numpy as np

MATRIX = np.array([[1, 1],
                   [1, 0]],
                  np.dtype('object'))


def solve(n: int) -> int:
    if n <= 0:
        return n

    return solve2(n)[0][1]


def solve2(n: int) -> np.ndarray:
    if n <= 1:
        return MATRIX

    if n & 1:
        temp = solve2((n - 1) // 2)
        return np.matmul(np.matmul(temp, temp), MATRIX)

    temp = solve2(n // 2)
    return np.matmul(temp, temp)


if __name__ == '__main__':
    print(solve(523))
