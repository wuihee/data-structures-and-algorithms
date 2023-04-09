"""
Isomorphic Trees

Give two undirected trees, identify if they are isomorphic, i.e. structurally
similar.

Algorithm
    1. Root trees.
    2. Identify their respective center nodes.
    3. Generate a string encoding for each tree and check for equality.
"""


def isIsomorphic(tree1, tree2):
    """
    Return if trees are isomorphic. Trees are represented by adjacency lists.
    """

    tree1_centers = findCenters(tree1)
    tree2_centers = findCenters(tree2)

    tree1_rooted = rootTree(tree1, tree1_centers[0])
    tree1_encoded = encode(tree1_rooted)

    for center in tree2_centers:
        tree2_rooted = rootTree(tree2, center)
        tree2_encoded = encode(tree2_rooted)
        if tree1_encoded == tree2_encoded:
            return True

    return False


def encode(node):
    """
    Return a string encoding for the subtree rooted at node.

    Parameters
    ----------
    node : Node object.
    """

    if not node:
        return ""

    labels = []
    for children in node:
        labels.append(encode(children))
    labels.sort()

    return "(" + ''.join(labels) + ")"


def findCenters(tree):
    """
    Return the center of value of the tree center.

    Parameters
    ----------
    tree : Adjacency list representation of the tree, where nodes are uniquely
           numbered. tree[i] references the nodes that node i is connected to.
    """

    n = len(tree)
    degrees = [len(tree[i]) for i in range(n)]
    leaves = []

    while leaves:

        for i in range(n):
            if degrees[i] == 1:
                leaves.append(i)

        for i in leaves:

            # Reduce degrees of connected nodes by 1.
            for j in tree[i]:
                degrees[j] -= 1

            # Remove leaf.
            tree[i] = []


def rootTree(tree, center):
    pass
