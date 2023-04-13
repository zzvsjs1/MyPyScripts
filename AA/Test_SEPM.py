def subset_sum(numbers, target, res: list, partial=None):
    if partial is None:
        partial = []

    s = sum(partial)

    if s == target:
        res.append(partial)

    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, res, partial + [n])


if __name__ == '__main__':
    res = []
    subset_sum([5, 6, 7], 18, res)
    print(res)
