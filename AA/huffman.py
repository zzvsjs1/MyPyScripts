from queue import PriorityQueue


class NN:

    def __init__(self, s, f, left, right):
        self.symbol = s
        self.frequency = f
        self.left_child = left
        self.right_child = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency


class HuffmanCoding:

    ASCII_SIZE = 256

    @staticmethod
    def build_tree(inputString):
        # convert string to a character array
        input_char_seq = list(inputString)

        # dict to store the frequency of the symbols
        freq = [0] * HuffmanCoding.ASCII_SIZE

        # compute the frequencies
        for i in range(len(input_char_seq)):
            freq[ord(input_char_seq[i])] += 1

        # build tree
        # initialise priority queue with the leaf nodes
        priority_q = PriorityQueue()
        for i in range(len(freq)):
            if freq[i] > 0:
                priority_q.put(NN(chr(i), freq[i], None, None))

        # loop through priority queue, merging the dequeued nodes with next smallest
        while priority_q.qsize() > 1:
            left = priority_q.get()
            right = priority_q.get()

            # merge the two nodes, and use null character '\0' as character of
            # parent node
            new_parent = NN(None, left.frequency + right.frequency, left, right)
            # put this new parent node back into priority queue
            priority_q.put(new_parent)

        # remove remaining node as the root of the huffman tree
        root = priority_q.get()

        return root

    def assign_codeword(self, r):
        """
        * Assign codewords to the leaf nodes/symbols.
        *
        * @param root Root node of constructed Huffman tree.
        *
        * @return A map of each symbol/character to the assigned codeword.
        """
        mmm = {}

        # start the recursive tree traversal from root to assign codewords
        self.recursive_assign_codeword(mmm, r, '')

        return mmm

    @staticmethod
    def recursive_assign_codeword(code_map, cur: 'NN', curr_code_str):
        if cur is not None and cur.left_child is None and cur.right_child is None:
            code_map[cur.symbol] = curr_code_str
            return

        HuffmanCoding.recursive_assign_codeword(code_map, cur.left_child, curr_code_str + '0')
        HuffmanCoding.recursive_assign_codeword(code_map, cur.right_child, curr_code_str + '1')


if __name__ == "__main__":
    input_string = input('Enter string: ')

    coding = HuffmanCoding()
    root = coding.build_tree(input_string)

    # assign codewords
    code_map = coding.assign_codeword(root)

    print()

    # print out the codeword map
    print("Applying Huffman coding, the following map is obtained: ")
    for key, value in code_map.items():
        print(f"{key} -> {value}")

    print()

    # print out original string and same string encoded with the generated
    # Huffman code
    print("Original string encoded with this prefix code is:")
    input_char_seq = list(input_string)
    buffer = [code_map[char] for char in input_char_seq if char is not None]

    print()
    print("".join(buffer))
