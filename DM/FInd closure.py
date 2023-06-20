import re
import numpy as np
from typing import List, Set, Tuple

A_DEGIT = ord('a')


def find_reflexive(m: list[list[int]]) -> Set[Tuple[str, str]]:
    assert len(m) > 0
    ret = set()
    for i in range(len(m)):
        ret.add((chr(A_DEGIT + i), chr(A_DEGIT + i)))

    return ret


def find_symmetric(m: List[List[int]]):
    ret = set()
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            if i == j:
                continue

            if cell == 1:
                ret.add((chr(A_DEGIT + i), chr(A_DEGIT + j)))
                ret.add((chr(A_DEGIT + j), chr(A_DEGIT + i)))

    return ret


# Warshall’s Algorithm
def find_transitive(m: List[List[int]]) -> np.ndarray:
    assert len(m) > 0
    assert len(m) == len(m[0])

    mr = np.asanyarray(m)
    w = mr.copy()

    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                w[i][j] |= (w[i][k] & w[k][j])

    return w


def set_tuple_list_to_2d_list(var: List[tuple[str, str]]) -> tuple[set[str], [[str]]]:
    # s = set()
    s = {'a', 'b', 'c', 'd'}

    for i in var:
        for j in i:
            s.add(j)

    ret = [[0 for _ in s] for _ in s]

    for i in var:
        ret[ord(i[0]) - A_DEGIT][ord(i[1]) - A_DEGIT] = 1

    return s, ret


# Pass a string set to a list, which contain tuple like (str, str)
def pass_set(string: str) -> List[tuple[str, str]]:
    regex = re.compile(r'\(\w+,\w+\)')
    string = string.replace('{', '').replace('}', '').replace(' ', '')
    data = regex.findall(string)
    ret = []
    for i in data:
        tmp = i.replace('(', '').replace(')', '')
        tmp = tmp.split(',')
        ret.append((tmp[0], tmp[1]))

    return ret


def matrix_ndarray_to_set(m: np.ndarray):
    ret = set()
    for i, data in enumerate(m):
        for j, data_inner in enumerate(data):
            if data_inner == 1:
                ret.add((chr(A_DEGIT + i), chr(A_DEGIT + j)))

    return ret


def set_to_list_and_sort(s: set) -> []:
    l = list(s)
    l.sort()
    return l


def what_we_need_to_add(s1: set, s2: set) -> set:
    return s1.difference(s2)


def assign_set_to_matrix(l: [Tuple[str, str]], n: int):
    ret = [[0 for _ in range(n)] for _ in range(n)]

    for a, b in l:
        ret[ord(a) - A_DEGIT][ord(b) - A_DEGIT] = 1

    return ret


if __name__ == '__main__':
    while True:
        input_list_tuple = pass_set(input('Enter sets: '))

        input_list_tuple_set = set(input_list_tuple)

        all_set_elements, matrix = set_tuple_list_to_2d_list(input_list_tuple)

        # Find reflexive
        reflexive_tuple_set = find_reflexive(matrix)

        reflexive_tuple_set2 = reflexive_tuple_set.difference(input_list_tuple_set)
        reflexive_result = set_to_list_and_sort(reflexive_tuple_set2)

        # Find symmetric
        symmetric_tuple_set = find_symmetric(matrix)

        symmetric_tuple_set2 = symmetric_tuple_set.difference(input_list_tuple_set)
        symmetric_result = set_to_list_and_sort(symmetric_tuple_set2)

        # Find transitive
        transitive_ndarray = find_transitive(matrix)

        transitive_set = matrix_ndarray_to_set(transitive_ndarray)

        transitive_set2 = what_we_need_to_add(transitive_set, input_list_tuple_set)
        transitive_result = set_to_list_and_sort(transitive_set2)

        # equivalence
        all_union_set = input_list_tuple_set.union(reflexive_tuple_set, symmetric_tuple_set, transitive_set)
        all_union_matrix = assign_set_to_matrix(all_union_set, len(matrix))

        all_union_symmetric_set = find_symmetric(all_union_matrix)
        a = all_union_symmetric_set.union(all_union_set)

        equivalence_res_set = a.difference(input_list_tuple_set)
        equivalence_res = set_to_list_and_sort(equivalence_res_set)

        # Print results

        print(f'Reflexive: \n {reflexive_result}\n')
        print(f'Symmetric: \n {symmetric_result}\n')
        print(f'Transitive: \n {transitive_result}\n')
        print(f'Equivalence: \n {equivalence_res}\n')
        print(f'Is Reflexive: {len(reflexive_result) == 0}')
        print(f'Is Symmetric: {len(symmetric_result) == 0}')
        print(f'Is Transitive: {len(transitive_result) == 0}')
        print()
        # break
