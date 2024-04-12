"""
Depth-First Search (DFS) Algorithm for Binary Trees: 
- DFS is performed by traversing to the leaf nodes. It goes as deep as it can, then moves on to the next branch.
- DFS can be implemented using a stack or recursion. 

DFS Traversals: 
1. Pre-order traversal: Visit the node, recursively traverse the left subtree, recursively traverse the right subtree.
2. In-order traversal: Recursively traverse the left subtree, visit the node, recursively traverse the right subtree.
3. Post-order traversal: Recursively traverse the left subtree, recursively traverse the right subtree, visit the node. 

Iterative implementation with a Stack (easiest -> pre-order):
- Push the right child first, then the left child
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    res = []
    if root:
        res.append(root.val)
        res += preorder(root.left)
        res += preorder(root.right)
    return res

def inorder(root):
    res = []
    if root:
        res += inorder(root.left)
        res.append(root.val)
        res += inorder(root.right)
    return res

def postorder(root):
    res = []
    if root:
        res += postorder(root.left)
        res += postorder(root.right)
        res.append(root.val)
    return res


if __name__ == "__main__":

    # sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1, Node(2, Node(4), Node(5)), Node(3))

    expected_preorder = [1, 2, 4, 5, 3]
    expected_inorder = [4, 2, 5, 1, 3]
    expected_postorder = [4, 5, 2, 3, 1]

    assert preorder(root) == expected_preorder
    assert inorder(root) == expected_inorder
    assert postorder(root) == expected_postorder

    print("All tests passed!")
