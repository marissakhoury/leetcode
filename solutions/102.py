"""
Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    res = []
    curr_level_queue = [root] # curr_level_queue will contain all the nodes in <level>
 
    while curr_level_queue:
        level_size = len(curr_level_queue)
        curr_level_nodes = [] # store nodes values at curr level 
        for _ in range(level_size):
            node = curr_level_queue.pop(0)
            curr_level_nodes.append(node.val)
            if node.left:
                curr_level_queue.append(node.left) 
            if node.right:
                curr_level_queue.append(node.right) 
        res.append(curr_level_nodes)

    return res

from collections import deque
def level_order(root):
    res = []
    q = deque()
    q.append(root)
    while q:
        q_len = len(q)
        level = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.left.left = Node(5)
root.right.left = Node(15)
root.right.right = Node(7)

if __name__ == "__main__":
    assert level_order(root) == [[3], [9, 20], [5, 15, 7]]
    print('Passed!')

