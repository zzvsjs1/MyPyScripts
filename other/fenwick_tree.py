class FenwickTree:

    data: []

    def __init__(self, n: int):
        self.data = [0] * (n + 1)

    @staticmethod
    def __parent__(i: int) -> int:
        return i - (i & (-i))



    def __str__(self):
        return str(self.data)