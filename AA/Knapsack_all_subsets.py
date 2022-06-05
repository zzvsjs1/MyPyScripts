import re
from rich.console import Console

c = Console()


def get_index(inl: int) -> list:
    # index = 0
    # ret = []
    # while inl >> index != 0:
    #     if (1 << index) & inl != 0:
    #         ret.append(index)
    #     index += 1
    # return ret
    val = bin(inl).replace('0b', '')
    return [i for i, s in zip(range(len(val)), reversed(val)) if s == '1']


def solve(a: list, n: int):
    print()

    num = 0
    max_weight = -1
    for i in range(2 ** len(a)):
        temp = [a[i] for i in get_index(i)]
        su = sum(temp)
        if su > max_weight:
            max_weight = su
        if su <= n:
            c.print(f'Subset: {temp} Total weight: {su}', style='red')
            num += 1

    print()
    c.print(f'Total subsets (include empty): {num}', style='red')
    c.print(f'Total subsets (exclude empty): {num - 1}', style='red')
    c.print(f'Maximum weight: {max_weight}', style='red')


if __name__ == '__main__':
    solve(list(map(int, [tu for tu in re.findall(r'(\w+) *',
                                                 input('Enter weight\n'
                                                       'Split by comma or space\n'
                                                       'enter: '))])), int(input('n: ')))
