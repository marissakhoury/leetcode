""""
Problem Link: https://leetcode.com/problems/symmetric-tree/

Time Complexity: O(n), visiting each node exactly once. 
Space Complexity: O(h), where h is the height of the tree just like with any DFS algorithm.
Note: Space compexity primarily depends on the recursion call stack (which in the worst case could be as deep as the height of the tree). 
- In a balanced tree, this would be log(n), where n is the number of nodes 
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    def dfs(left, right):
        """
        Inner function to perform depth-first search (DFS) on two subtrees to check for symmetry.
        """
        # base case: both trees are empty
        if not left and not right: 
            return True
        # base case: one tree is empty, other is not --> trees not symmetric
        if not left or not right:
            return False
        # Check if current nodes are equal and recurse on the children (mirrored so dfs(inner children), dfs(outer children))
        return ((left.val == right.val) and 
        (dfs(left.left, right.right)) and
        (dfs(left.right, right.left)))
    # edge case: an empty tree is considered symmetric
    if not root:
        return True
    # start the dfs from the root's left and right children
    return dfs(root.left, root.right)


if __name__ == "__main__":
    # Example 1: Symmetric tree [1,2,2,3,4,4,3]
    root1 = Node(1)
    root1.left = Node(2, Node(3), Node(4))
    root1.right = Node(2, Node(4), Node(3))
    assert is_symmetric(root1) == True

    # Example 2: Asymmetric tree [1,2,2,None,3,None,3]
    root2 = Node(1)
    root2.left = Node(2, None, Node(3))
    root2.right = Node(2, None, Node(3))
    assert is_symmetric(root2) == False

    # Example 3: Symmetric single-node tree [1]
    root3 = Node(1)
    assert is_symmetric(root3) == True

    # Example 4: Empty tree []
    root4 = None
    assert is_symmetric(root4) == True

    print("All test cases passed!")