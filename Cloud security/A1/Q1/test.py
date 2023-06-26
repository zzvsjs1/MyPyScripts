from functools import reduce

while True:
    num = int(input('Enter number: '))
    t = list(set(reduce(list.__add__,
                        ([i, num // i] for i in range(1, int(num ** 0.5) + 1) if num % i == 0))))
    t.sort()
    a = t.__repr__()
    print(a[1:len(a) - 1])
    print()
