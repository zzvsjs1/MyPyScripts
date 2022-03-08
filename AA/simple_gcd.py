def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)