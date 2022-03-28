import sys

with open(sys.argv[1], 'r') as file:
    lines: str = file.read()
    temp = 0
    for each in sys.argv[2]:
        temp += lines.count(each)
    print(temp)
