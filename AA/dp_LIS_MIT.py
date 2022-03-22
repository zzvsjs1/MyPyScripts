# MIT 6.006 Introduction to Algorithms, Spring 2020
# see: https://www.youtube.com/watch?v=r4-cftqTcdI&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=42

def solve_suffix(string: str):
    l = [0] * len(string)
    max_e1 = 0
    for i in reversed(range(len(string))):
        max_e = 0
        for j in range(i + 1, len(string)):
            if string[i] < string[j] and l[j] > max_e:
                max_e = l[j]

        l[i] = max_e + 1
        if l[i] > max_e1:
            max_e1 = l[i]

    print(max_e1)


def solve_prefix(string: str):
    pass


if __name__ == '__main__':
    my_string = 'CARBOHYDRATE'
    solve_suffix(my_string)
