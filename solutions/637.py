"""
Problem Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def average_of_levels_binary_tree(root):
    level_averages = []
    q = []
    q.append(root) 
    while q:
        len_q = len(q) 
        curr_level = []
        for i in range(len_q):
            node = q.pop(0) 
            if node:
                curr_level.append(node.val) 
                q.append(node.left) 
                q.append(node.right) 
        if curr_level:
            avg_level = sum(curr_level) / len(curr_level)
            level_averages.append(avg_level)
    return level_averages


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

if __name__ == "__main__":
    assert average_of_levels_binary_tree(root) == [3.0, 14.5, 11.0]
    print('Passed!')