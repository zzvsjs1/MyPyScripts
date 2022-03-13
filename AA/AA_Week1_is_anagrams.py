def is_anagrams(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False

    temp_dir1 = {}

    for i, j in zip(a, b):
        if i not in temp_dir1:
            temp_dir1[i] = 0
        if j not in temp_dir1:
            temp_dir1[j] = 0

        temp_dir1[i] += 1
        temp_dir1[j] -= 1

    for k, v in temp_dir1.items():
        if v != 0:
            return False

    return True


if __name__ == '__main__':
    print(is_anagrams("aaasssdddfffggghhhjjjkkklll", "lllkkkjjjhhhgggfffdddsssaaa"))
