from pymouse import PyMouse
from time import sleep

m = PyMouse()
left = True

for _ in range(1000):
    if left:
        m.click(1027, 1020, 1)
    # else:
    #     m.click(1083, 1026, 1)
    # left = not left
    sleep(0.2)


# from pynput import *
#
# def get_coords(x, y):
#     print(f'{x} {y}')
#
# with mouse.Listener(on_move=get_coords) as l:
#     l.join()
