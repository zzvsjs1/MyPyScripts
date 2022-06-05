import re


def do_insertion_sort(a: list):
    step: int = 0
    compare = 0
    for i in range(len(a)):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            compare += 1
            a[j + 1] = a[j]
            print(f'Step {step}: {a}')
            step += 1
            j -= 1

        a[j + 1] = v
        print(f'Step {step}: {a}')
        j -= 1
        step += 1

    print(f'Compare {compare}')


if __name__ == '__main__':
    in_str = input('Enter data\n'
                   'Split by comma or space\n'
                   'enter: ')

    m = [tu for tu in re.findall(r'(-?\w+) *', in_str)]
    ty = input('Data type: ')
    exec(f'm = list(map({ty}, m))')

    do_insertion_sort(m)
