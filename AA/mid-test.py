import re


def solve(a: list) -> list:
    j = 0
    for i in range(1, len(a)):
        if a[i] < 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    return a


if __name__ == "__main__":
    in_str = input('Enter a list of number\n'
                   'format: 1, 2, 3\n'
                   'enter: ')
    m = list(map(int, re.findall(r'\d+|-\d+', in_str)))
    print(solve(m))
