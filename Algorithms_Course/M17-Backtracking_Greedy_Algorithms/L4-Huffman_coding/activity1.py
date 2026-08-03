import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left or current node
        self.left = left

        # node right or current node
        self.right = right

        # true direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

# utility function to print huffman
# codes for all symbols in the newly
# created huffman tree
def printHodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printHodes(node.left, newVal)
    if(node.right):
        printHodes(node.right, newVal)

    # if node is edge node then
    # display its huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

# characters for huffman tree
chars = ['e', 'b', 'c', 'd', 'a', 'f']

# frequency of characters
freq = [5, 9, 12, 13, 16, 45]

# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:

    # sort all the nodes in ascending order
    # based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    # assign directional value to those nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # a new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    heapq.heappush(nodes, newNode)

# huffman Tree is ready!
printHodes(nodes[0])