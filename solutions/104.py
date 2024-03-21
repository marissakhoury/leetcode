""""
Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Longest Path from Root to Leaf Node

Solution 1: Recursive DFS
Time Complexity: O(n), traversing entire tree.
Space Complexity: O(n). 
---------------------------------------------------------------------------------------------
Solution 2: Iterative BFS (Level order traversal)
- Idea: we first walk through all nodes on the same level before moving on to the next level  
- BFS uses QUEUE data structure (FIFO)

Time Complexity: O(n), traversing entire tree.
Space Complexity: O(n). 
---------------------------------------------------------------------------------------------
Solution 3: Iterative DFS
- Use STACK data structure
- Implement PREORDER (Root, Left, Right) with STACK because it is by far easiest traversal to do iteratively
- Visit every node, find node with greatest depth and return that
- Stack holds [node, depth]

Time Complexity: O(n), traversing entire tree.
Space Complexity: O(n). 
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursive_dfs_max_depth(root):
    """
    Solution 1: Recursive DFS
    Think: 1 + max(max_depth(left_subtree), max_depth(right_subtree))
    """
    # base case
    if not root:
        return 0
    # recursive case
    return 1 + max(recursive_dfs_max_depth(root.left), recursive_dfs_max_depth(root.right))

from collections import deque
def bfs_max_depth(root):
    """
    Solution 2: Iterative BFS
    Think: Keep count of number of levels (which is max_depth)
    """
    if not root:
        return 0
    level = 0
    q = deque([root])
    while q:
        
        for i in range(len(q)): # snapshot of length of q at this current time
            node = q.popleft() # pop from left

            if node.left: # if node.left is not null
                q.append(node.left) # add from right

            if node.right: # if node.right is not null
                q.append(node.right) # add from right

        level += 1
    return level

def dfs_max_depth(root):
    """
    Solution 3: Iterative DFS
    Stack with Preorder DFS 
    """
    if not root:
        return 0
    stack = [[root, 1]]
    result = 1

    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)   
            stack.append([node.left, depth + 1]) # add children nodes and depth
            stack.append([node.right, depth + 1])
    return result


if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    assert recursive_dfs_max_depth(root) == 3
    assert bfs_max_depth(root) == 3
    assert dfs_max_depth(root) ==  3
    print('All passed!')

