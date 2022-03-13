import math


def compute(r: int, n: int):
    if n <= r:
        raise ValueError('Not allow')

    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


if __name__ == '__main__':
    print(f'{compute(int(input("R: ")), int(input("N: ")))}')
