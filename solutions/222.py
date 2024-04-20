"""
Problem Link: https://leetcode.com/problems/count-complete-tree-nodes/

Perfect Binary Tree: Every level is fully populated

        1           - Height from the root (not counting the root itself) is 2 
       / \          - Total levels including the root are 3
      2   3
     / \ / \
    4  5 6  7
number of nodes = 2^(h+1) - 1


Complete Binary Tree (but not perfect binary tree):
Fully filled except possibly for the last level which is filled from left -> right

        1
       / \
      2   3
     / \
    4   5
Node count formula when left and right subtree heights are NOT equal: 
number of nodes = 1 + count of nodes in the left subtree + count of nodes in the right subtree 
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def count_nodes(root):
    """
    Simple recursive DFS approach
    Time Complexity: O(N)
    """
    if not root:
        return 0
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    return 1 + left_count + right_count

def count_nodes_2(root):
    """
    Optimized solution
    Time Complexity: O(logN * logN)
    """
    if not root:
        return 0
    
    # function to calculate height by continuously moving left 
    def left_height(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    # function to calculate height by continuously moving right 
    def right_height(node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
    
    # calculate the heights of left and right subtrees of the root
    left_height = left_height(root.left)
    right_height = right_height(root.right)

    # if the two heights are the same
    if left_height == right_height:
        # means the left subtree is perfect binary tree
        return 2**(left_height + 1) - 1
    else:
        # heights differ, so recursively count nodes on both subtrees and add 1 for the root node
        return 1 + count_nodes_2(root.left) + count_nodes_2(root.right)
    
if __name__ == "__main__":
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
    assert count_nodes(root) == 6
    print('Passed!')

    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
    assert count_nodes_2(root) == 6
    print('Passed!')