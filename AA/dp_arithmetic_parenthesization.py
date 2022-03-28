def solve(lin: str):
    lin = lin.replace(' ', '')



    eval(f'print({lin})', globals(), locals())


if __name__ == '__main__':
    solve('7 - 4 * 3 - 5')

