import math


def compute(r: int, n: int) -> int:
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


if __name__ == '__main__':
    print(f'{compute(int(input("R: ")), int(input("N: ")))}')
