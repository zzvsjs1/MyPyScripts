from abc import ABC
from typing import Sequence


class Range(Sequence[int], ABC):

    index: int

    start: int

    length: int

    step: int

    @staticmethod
    def __compute_range_length(start: int, stop: int, step: int):
        if step > 0 and start < stop:
            return 1 + (stop - 1 - start) // step

        if step < 0 and start > stop:
            return 1 + (start - 1 - stop) // -step

        return 0

    def __init__(self, start: int, stop: int, step: int = 1):
        self.index = 0
        self.start = start
        self.step = step
        self.length = Range.__compute_range_length(start, stop, step)

    def __iter__(self):
        return RangeIter(self.start, 0, self.length, self.step)

    def __reversed__(self):
        return Range(self.start + (self.length - 1) * self.step,
                     self.start - self.step,
                     -self.step)

    def __getitem__(self, item):
        if item >= self.__stop() or item < self.start:
            raise RuntimeError('{} out of range.'.format(item))

        return self.start + self.index * item * self.step

    def index(self, value: int, **kwargs):
        if value < self.start or value >= self.__stop():
            raise ValueError('{} is not in range.')

        return value

    def __stop(self):
        return self.start + self.length * self.step

    def __len__(self):
        return self.length

    def __hash__(self):
        return hash((self.index, self.start, self.__stop(), self.step))

    def __str__(self):
        return 'Range({}, {}, {})'.format(self.start, self.__stop(), self.step)


class RangeIter:

    start: int

    index: int

    length: int

    step: int

    def __init__(self, start: int, index: int, length: int, step: int):
        self.start = start
        self.index = index
        self.length = length
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration

        ret: int = self.start + self.index * self.step
        self.index += 1
        return ret

    def __len__(self):
        return self.length

    def __str__(self):
        return 'RangeIter[{}, {})'.format(self.start, self.start + self.length * self.step)


print(list(reversed(range(5, 20, 10))))
print(list(reversed(Range(5, 20, 10))))
