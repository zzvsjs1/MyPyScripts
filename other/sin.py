import math


def my_sin(s: float) -> float:
    theta = (s + math.pi) % (2 * math.pi) - math.pi
    result = 0
    term_sign = 1
    power = 1

    for i in range(10):
        result += (theta ** power / math.factorial(power)) * term_sign
        term_sign = -term_sign
        power += 2

    return result


print(my_sin(101))
print(math.sin(101))
