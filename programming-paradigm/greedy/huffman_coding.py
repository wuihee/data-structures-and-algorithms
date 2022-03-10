"""
Huffman Coding

A lossless data compression algorithm. Given a string of text, return
corresponding binary encoding for each unique character in the string.
"""

import heapq
from collections import Counter


class MinHeap:
    """heapq with custom compare predicate via key=."""

    def __init__(self, initial=None, key=lambda x: x):
        """
        Initialize heap object.

        Parameters
        ----------
        initial : List of comparable elements to build the heap with.
        key : Function used to compare elements in the heap by, e.g. len().
        """

        # self.index is used to make sure heapify doesn't return an error in
        # the case that the first element in the tuple (key(item), i, item)
        # are the same.
        self.index = 0
        self.key = key

        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            self.length = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []
            self.length = 0

    def push(self, item):
        """
        Push item onto the heap.

        Parameters
        ----------
        item : Same-type object to be pushed onto the heap.
        """
        heapq.heappush(self._data, (self.key(item), self.index, item))
        self.index += 1
        self.length += 1

    def pop(self):
        """Pop off the minimum item from the heap."""
        self.length -= 1
        return heapq.heappop(self._data)[2]


class Node:
    """Node class to represent each node in the Huffman Tree."""

    def __init__(self, freq, char=None, left=None, right=None):
        """
        Initialize the node with the following attributes.

        Parameters
        ----------
        freq : The frequency of the character in the given text.
        char : The ASCII character.
        left : Left child of the node.
        right : Right child of the node.
        """
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
        # Huff value is either a '0' or '1' depending if node is a left or
        # right child.
        self.huff = ''


def build_huffman_tree(S):
    """
    Build a huffman tree from string S.

    Paramters
    ---------
    S : String of characters.
    """

    # Map each character to it's respective frequency and store it in a dict.
    freqs = Counter(S)

    # Build min-heap based on the frequency of each character.
    heap = [Node(freqs[i], i) for i in freqs]
    heap = MinHeap(heap, key=lambda x: x.freq)

    # Build Huffman Tree.
    while heap.length > 1:

        # Pop two smallest nodes.
        node_1 = heap.pop()
        node_2 = heap.pop()

        # Assign huff values and merge to create a new node.
        node_1.huff = '0'
        node_2.huff = '1'
        new_node = Node(node_1.freq + node_2.freq, None, node_1, node_2)

        # Push the new node back into the heap.
        heap.push(new_node)

    # Final node is the root of the Huffman tree.
    root = heap.pop()
    return root


def huffman_coding(node: Node, code='') -> dict:
    """
    Recrusively return respective codewords for each character.

    Parameters
    ----------
    node : Root of the current subtree.
    code : The current binary code up till now in the recursive call.
    """
    coding = {}
    new_code = code + node.huff

    # Base Case: Leaf node.
    if not node.left and not node.right:
        coding[node.char] = new_code

    if node.left:
        coding.update(huffman_coding(node.left, new_code))
    if node.right:
        coding.update(huffman_coding(node.right, new_code))

    return coding
