def solve(maze: [[int]]):
    solve2(0, 0, len(maze) - 1, len(maze) - 1, maze)
    return maze


def solve2(y1: int, x1: int, y2: int, x2: int, maze: [[int]]):
    if y2 - y1 < 1 or x2 - x1 < 1:
        return

    solve2(y1, x1, y2 // 2, x2 // 2, maze)
    solve2(y1, (x2 + 1) // 2, x2, y2 // 2, maze)
    solve2((y2 + 1) // 2, x1, y2, x2 // 2, maze)
    solve2((y1 + 1) // 2, (x1 + 1) // 2, y2, x2, maze)


if __name__ == '__main__':
    a = solve(
       [[0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
    )

    for i in a:
        print(i)
