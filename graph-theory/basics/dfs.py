class Node:
    """This is the structure of a Node object."""
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def inorder(root):
    """
    In-Order Traversal Algorithm:
        1. Traverse left subtree.
        2. Visit root.
        3. Traverse right subtree.

    Used for getting the nodes in a BST in order, expression evaluation,
    building a threaded binary tree, checking for a BST, and finding the
    median of a BST.

    Also known as level order traversal.
    """
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    """
    Pre-Order Traversal Algorithm:
        1. Visit root.
        2. Traverse left subtree.
        3. Traverse right subtree.

    Used for creating a copy of the tree.
    """
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """
    Post-Order Traversal Algorithm:
        1. Traverse right subtree.
        2. Traverse left subtree.
        3. Visit root.

    Used for deleting the tree, expression evaluation, finding the height of
    a binary tree, finding the diameter of a binary tree, or checking for a
    full binary tree.
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
