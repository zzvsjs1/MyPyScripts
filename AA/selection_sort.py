import re


def do_selection_sort(in_list: list):
    for i in range(len(in_list)):
        print(f'Step {i}: {in_list}')
        minimum = i
        for j in range(i, len(in_list)):
            if in_list[j] < in_list[minimum]:
                minimum = j

        in_list[i], in_list[minimum] = in_list[minimum], in_list[i]


if __name__ == "__main__":
    in_str = input('Enter a list of number\n'
                   'format: 1, 2, 3\n'
                   'enter: ')
    m = list(map(int, re.findall(r'\d+', in_str)))
    do_selection_sort(m)
