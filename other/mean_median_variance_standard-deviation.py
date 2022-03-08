import re
from decimal import Decimal


def get(ilist: list[Decimal]):
    len_of_list: int = len(ilist)
    if len_of_list == 0:
        return 0, 0, 0, 0, 0

    if len_of_list <= 1:
        return ilist[0], ilist[0], ilist[0], 0, 0

    ilist.sort()

    lsum: Decimal = sum(ilist)
    mean: Decimal = lsum / len_of_list
    median: Decimal = ilist[len_of_list // 2 + 1] \
        if len_of_list & 1 \
        else (ilist[len_of_list // 2] + ilist[len_of_list // 2 + 1]) / Decimal('2')

    variance: Decimal = Decimal('0')
    for i in ilist:
        variance += (i - mean) ** 2

    variance = variance / (len_of_list - 1)

    return lsum, mean, median, variance, variance.sqrt()


if __name__ == '__main__':
    input_str = input('Get input list: ')
    out_list = re.findall(r'\d+', input_str)
    out_list = list(map(Decimal, out_list))
    a, b, c, d, e = get(out_list)
    print(f'Sum: {a}\n'
          f'Mean: {b}\n'
          f'Median: {c}\n'
          f'Variance: {d}\n'
          f'Standard Deviation: {e}')
