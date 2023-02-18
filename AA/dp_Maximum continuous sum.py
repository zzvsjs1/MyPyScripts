def silly_method(data: []):
    _sum = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            temp = 0
            for k in range(i, j + 1):
                temp += data[k]
                if temp > _sum:
                    _sum = temp

    return _sum


def good_method(data: []):
    prev = 0
    _max = data[0]
    for i in data:
        prev = max(prev + i, i)
        _max = max(prev, _max)

    return _max


d = [-2, 11, -4, 13, -5, -2]
print(silly_method(d))
print(good_method(d))
