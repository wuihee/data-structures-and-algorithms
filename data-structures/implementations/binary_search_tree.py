class Node:
    """
    Node object found in BST.

    Attributes
    ----------
    key : The value of the node.
    parent : Refereces the parent node.
    left : Refereces the left child.
    right : References the right child.
    """

    def __init__(self, key, parent=None, left=None, right=None):
        """Initializes Node object with it's attributes."""
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    Initialize a binary search tree with a root.

    Attributes
    ----------
    root : The root of the BST

    Methods
    -------
    print_inorder(node) : Prints the BST in sorted order via inorder traversal.
    search(root, key) : Searches BST with root for specified key.
    get_min(root) : Returns the node with the smallest key.
    get_max(root) : Returns node with the largest key.
    successor(node) : Return the smallest node with key greater than node.key.
    insert(root, node) : Insert node in BST.
    transplant(root, u, v) : Replace subtree rooted at u with subtree at v.
    delete(root, node) : Delete node from BST.
    """

    def __init__(self, root):
        """
        Initializes the root of the BST.

        Parameters
        ----------
        root : Node object.
        """

        self.root = root

    def print_inorder(self, root):
        """
        Prints the BST in sorted order via inorder traversal.

        Parameters
        ----------
        root : Root of the BST (or subtree) to start traversing from.
        """

        # Terminate once function has traversed all the way down BST.
        if not root:
            return
        else:
            self.print_inorder(root.left)
            print(root.key)
            self.print_inorder(root.right)

    def search(self, root, key):
        """
        Find and return node with specified key in BST.

        Parameters
        ----------
        root : Root of the BST (or subtree) to start searching from.
        key : Key of the node to be found.
        """

        # Continue searching while root is not empty and key is not found.
        while root and key != root.key:
            # Search left subtree if key is smaller than root.
            if key < root.key:
                root = root.left
            # Else, search right subtree if key is larger.
            else:
                root = root.right
        return root

    def get_min(self, root):
        """
        Returns the node with the smallest key in the BST.

        Parameters
        ----------
        root : Root of the BST (or subtree) to start searching from.
        """

        # Traverse down all the way left to find minimum node (BST property).
        while root.left:
            root = root.left
        return root

    def get_max(self, root):
        """
        Returns the node with the largest key in the BST.

        Parameters
        ----------
        root : Root of the BST (or subtree) to start searching from.
        """

        # Traverse down all the way right to find maximum node (BST property).
        while root.right:
            root = root.right
        return root

    def successor(self, node):
        """
        Given a node, return the smallest node with key greater than node.key.

        Parameters
        ----------
        node : Node object to take reference from.
        """

        # Return the smallest descendent on the right subtree, i.e. traverse
        # right and then left all the way.
        if node.right:
            return self.get_min(node.right)
        # However, if right subtree doesn't exist, return the right most
        # ancestor, i.e. from the current node, traverse left all the way
        # then right once.
        parent = node.parent
        while parent and node is parent.right:
            node = parent
            parent = parent.parent
        return parent

    def insert(self, root, node):
        """
        Given a node, insert it in the BST.

        Parameters
        ----------
        root : Root of the BST.
        node : Node to be inserted.
        """

        temp = None
        trav = root
        # Find the position where node should be inserted by applying a search
        # algorithm. Attempt to 'find' node to be inserted and traverse left or
        # right accordingly.
        while trav:
            temp = trav
            if node.key < trav.key:
                trav = trav.left
            else:
                trav = trav.right
        # temp points to the node right before trav hits None and is the
        # position of where the new node should be inserted. So far, the
        # pointer from the new node to it's parent has been established.
        node.parent = temp
        # Now, we have to establish the pointer from the parent node
        # (i.e. temp) to the new node.
        # If traversal didn't occur and temp is None, the tree was empty and
        # the new node will be the new root.
        if not temp:
            self.root = node
        # New node will be a left child if it's key is smaller than parent's.
        elif node.key < temp.key:
            temp.left = node
        # Otherwise, it's key is greater and will be a right child.
        else:
            temp.right = node

    def transplant(self, root, u, v):
        """
        Replaces the subtree rooted at u with the subtree rooted at v.

        Parameters
        ----------
        root : Root of the BST.
        u : Node object; root of subtree to be replaced.
        v : Node object; root of subtree replacing.
        """

        # Make v the root of the BST if u is the root.
        if not u.parent:
            self.root = v
        # Make v the appropriate child of u's parent.
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        # If v is not None, update v's parent as u's parent.
        if v:
            v.parent = u.parent

    def delete(self, root, node):
        """
        Given a node, delete it from the BST.

        Parameters
        ----------
        root : Root of the BST.
        node : Node to be deleted.
        """

        # Promote right child if left child doesn't exist.
        if not node.left:
            self.transplant(root, node, node.right)
        # Promote left child if right child doesn't exist.
        elif not node.right:
            self.transplant(root, node, node.left)
        # If both children exist,
        else:
            # Let y be the smallest node with a larger value than node which
            # will be replacing node. Note that y has no left child.
            y = self.get_min(node.right)
            # If y is not a direct child of node, we first replace y by it's
            # right child then replace node by y.
            if y.parent is not node:
                # First, replace y with it's own right child.
                self.transplant(root, y, y.right)
                # Next, replace node with y by attaching the right subtree of
                # node to y's right. Note that the current y.right is no longer
                # the previous y.right: y is now an independent node after
                # being transplanted.
                y.right = node.right
                # Update the parent of y's new right subtree as y.
                y.right.parent = y
            # If y is node's direct right child, simply replace node with y.
            self.transplant(root, node, y)
            # Update node's left subtree and connect it to y instead.
            y.left = node.left
            y.left.parent = y


class BSTAux:
    """
    Auxilliary class for BST. helps to easily call BST methods. Makes it such
    that user does not have to constantly input parameters into methods.

    Attributes
    ----------
    root : The root of the BST

    Methods
    -------
    print_inorder() : Prints the BST in sorted order via inorder traversal.
    search(key) : Searches BST with root for specified key.
    get_min() : Returns the node with the smallest key.
    get_max() : Returns node with the largest key.
    successor(key) : Return the smallest node with key greater than node.key.
    insert(key) : Insert node in BST.
    delete(key) : Delete node from BST.
    """

    def __init__(self, root):
        """Initialize the BST."""
        self.bst = BinarySearchTree(root)

    def print_inorder(self):
        """Prints the BST in sorted order via inorder traversal."""
        self.bst.print_inorder(self.bst.root)

    def search(self, key):
        """
        Searches BST and return node with specified key.

        Parameters
        ----------
        key : Key to search for.
        """
        return self.bst.search(self.bst.root, key)

    def get_min(self):
        """Return the node with the smallest key in the BST."""
        return self.bst.get_min(self.bst.root)

    def get_max(self):
        """Return the node with the largest key in the BST."""
        return self.bst.get_max(self.bst.root)

    def successor(self, key):
        """
        Given a key, return the smallest node with a larger key.

        Parameters
        ----------
        key : key to take reference from.
        """
        node = self.search(key)
        return self.bst.successor(node)

    def insert(self, key):
        """
        Insert given key into BST.

        Parameters
        ----------
        key : Key to insert into BST.
        """
        self.bst.insert(self.bst.root, Node(key))

    def delete(self, key):
        """
        Delete node with given key from BST.

        Parameters
        ----------
        key : Key to delete.
        """
        node = self.search(key)
        self.bst.delete(self.bst.root, node)
