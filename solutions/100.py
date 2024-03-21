"""
Problem Link: https://leetcode.com/problems/same-tree/

Solution: 
- Recursive DFS to traverse trees!

Time Complexity: O(p + q), worst case we traverse through both trees entirely. --> O(2N) = O(N)
Best case space complexity (completely balanced trees): O(log N) because nature of recursion.
Worst case space complexity (completely unbalanced trees): O(N).
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(p, q) -> bool:
    """
    Given the roots of two binary trees, p and q, check if they are identical.
    """
    # base case: if BOTH are empty, they are the same tree --> return True
    if not p and not q:
        return True
    # base case: if one is empty and the other is not --> return False
    if not p or not q:
        return False
    # base case: both have value but the values differ --> return False
    if p.val != q.val:
        return False
    # recursive step: if the left subtrees are the same AND right subtrees are the same --> returns True if AND is true
    return (is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right))

if __name__ == "__main__":
    # tree1 and tree2 are identical
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)

    tree2 = Node(1)
    tree2.left = Node(2)
    tree2.right = Node(3)

    # tree3 and tree4 are different
    tree3 = Node(1)
    tree3.left = Node(2)

    tree4 = Node(1)
    tree4.right = Node(2)

    assert is_same_tree(tree1, tree2)
    assert not is_same_tree(tree3, tree4)

    print('All tests passed!')