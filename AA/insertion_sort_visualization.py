import sys


def do_insertion_sort(ilist: list):
    step: int = 0
    for i in range(len(ilist)):
        v = ilist[i]
        j = i - 1
        while j >= 0 and ilist[j] > v:
            ilist[j + 1] = ilist[j]
            print(f'Step {step}: {ilist}')
            step += 1
            j -= 1

        ilist[j + 1] = v
        print(f'Step {step}: {ilist}')
        j -= 1
        step += 1


if __name__ == '__main__':
    do_insertion_sort(list(reversed(range(10))))
