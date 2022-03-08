class LetterFrequencyPair:

    def __init__(self, letter: str, frequency: int):
        self.letter: str = letter
        self.frequency: int = frequency

    def __str__(self):
        return '{}:{}'.format(self.letter, self.frequency)

class HTreeNode:
    pass

print(LetterFrequencyPair('A', 23))
