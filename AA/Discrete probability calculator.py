import re
import numpy as np


def cal(x: np.ndarray, px: np.ndarray):
    mean = (x * px).sum()
    variance = ((x - mean) ** 2 * px).sum()
    sd = np.sqrt(variance)
    print(f'Mean: {mean}')
    print(f'Variance: {variance}')
    print(f'SD: {sd}')


if __name__ == '__main__':
    x = np.array(list(map(float, re.findall(r'\S+', input('Enter x: ')))))
    px = np.array(list(map(float, re.findall(r'\S+', input('Enter p(x): ')))))
    cal(x, px)
