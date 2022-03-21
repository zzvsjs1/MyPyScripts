# MIT 6.006 Introduction to Algorithms, Spring 2020
# see: https://www.youtube.com/watch?v=r4-cftqTcdI&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=42

def solve_suffix(string: str, t: list):
    for i in reversed(range(len(string))):
        t[i] = 1 + max([solve_suffix(string, [0] * (len(string) - 1)) for j in range(i, len(string)) if string[i] < string[j]])
    return t

def solve_prefix(string: str):
    pass


if __name__ == '__main__':
    my_string = 'CARBOHYDRATE'
    li = [0] * (len(my_string) + 1)
    solve_suffix(my_string, li)
    print(li)
