"""
Problem Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Approach: 
- Need to put values from each "level" in an array --> BFS, use queue? 
- Levels at odd indices should go in REVERSE to follow zig zag traversal
- Levels at even indices should go Left -> Right (normal)

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
def zig_zag_traversal(root):
    """
    BFS
    """
    result = []
    q = deque([root] if root else []) 

    # BFS algo 
    while q: 
        level = [] 
        for i in range(len(q)): # snapshots the queue 
            node = q.popleft() 
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # every odd level needs to be reversed b/c zig zag
        level = list(reversed(level) if len(result) % 2 else level) # convert back to list b/c reversed returns an iterator
        result.append(level)
    return result 
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    assert zig_zag_traversal(root) == [[1], [3,2], [4,5,6]]
    print('Passed!')