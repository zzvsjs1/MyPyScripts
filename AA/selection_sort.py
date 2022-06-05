import re
from rich.console import Console


def do_selection_sort(in_list: list):
    for i in range(len(in_list)):
        print(f'Step {i}: {in_list}')
        minimum = i
        for j in range(i, len(in_list)):
            if in_list[j] < in_list[minimum]:
                minimum = j

        in_list[i], in_list[minimum] = in_list[minimum], in_list[i]


if __name__ == "__main__":
    console = Console()
    console.print(
        '''
        Selection sort is a brute force solution to the sorting problem. 
        
        1. Scan all n elements of the array to find the smallest element, 
        and swap it with the first element. 
        
        2. Starting with the second element, scan the remaining n - 1 elements to 
        find the smallest element and swap 
        it with the element in the second position. 
        
        3. Generally, on pass i(0 <= i <= n - 2), find the smallest 
        element in A[i...n - 1] and swap it with A[i].
        '''
    ,
        style="bold red")

    console.print('Selection sort only makes O(n) writes but O(n ^ 2) reads', style="red")
    console.print('Selection sort is NOT a stable sorting algorithm', end='\n\n', style="red")

    in_str = input('Enter data\n'
                   'Split by comma or space\n'
                   'enter: ')

    m = [tu for tu in re.findall(r'(-?\w+) *', in_str)]
    ty = input('Data type: ')
    exec(f'm = list(map({ty}, m))')

    do_selection_sort(m)
