class Node:
    """
    Node Object.
    """

    def __init__(self):
        """
        Initialize the attributes of the trie node object.
        """

        # Children is a dictionary of letters -> Node.
        self.children = {}

        # is_end denotes whether the current node is the end of a word.
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.

        Args:
            word (str): Word that we want to insert.
        """

        # Traverse the tree using the node object.
        node = self.root

        # Insert each letter into the trie.
        for letter in word:

            # If the current letter is already found, move to it.
            if letter in node.children:
                node = node.children[letter]

            # Otherwise, create a new branch on the trie.
            else:
                new_node = Node()
                node.children[letter] = new_node
                node = new_node

        # The final letter inserted is the end of the word.
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Searches for the given word in the trie.

        Args:
            word (str): The word we wish to search for.

        Returns:
            bool: Returns True if word is found, False otherwise.
        """

        # Traverse the trie with node.
        node = self.root

        for letter in word:
            if letter in node.children:
                node = node.children[letter]

            # If letter is not in children, it means the word doesn't exist.
            else:
                return False

        # Reaching the end of the word, we still don't know whether what we
        # have found is the enter word or just a prefix.
        return node.is_end
