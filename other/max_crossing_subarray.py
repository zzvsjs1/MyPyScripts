def max_crossing_subarray(my_list: list, low: int, height: int):
    if low == int or len(list) == 0:
        return low, height, list

    length: int = len(list)
    mid: int = int(length / 2)

    pass


def find_crossing_subarray(mylist: list, low: int, mid: int, height: int):
    left_sum = -0xffff_ffff_ffff_ffff
    my_sum = 0
    max_left = 0
    for i, j in zip(reversed(mylist[low:mid + 1]), range(mid + 1, low - 1, -1)):
        my_sum += i
        if my_sum > left_sum:
            left_sum = my_sum
            max_left = j

    right_sum = -0xffff_ffff_ffff_ffff
    my_sum = 0
    max_right = 0x0fff_ffff_ffff_ffff
    for i, j in zip(mylist[mid + 1:height], range(mid + 1, height)):
        my_sum += i
        if my_sum > right_sum:
            right_sum = my_sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


my_array: list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(find_crossing_subarray(my_array, 0, int(len(my_array) / 2), len(my_array)))
