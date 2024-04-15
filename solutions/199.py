"""
Problem Link: https://leetcode.com/problems/binary-tree-right-side-view/

- Imagine yourself standing on the right side of the tree, output should be all nodes you can see from the right
- BFS Implementation (level order traversal)
    - For each level of the tree, we want the rightmost node added to the output array
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root):
    if not root:
        return []
    q = [root]
    res = []

    while q:
        right_side = None
        level_length = len(q)

        for i in range(level_length):
            node = q.pop(0) # pop from left
            if node:
                right_side = node
                q.append(node.left) # add left node before adding right node to queue 
                q.append(node.right)

        if right_side:
            res.append(right_side.val)
            
    return res
               
if __name__ == "__main__":
    # input: [1,2,3,null,5,null,4]
    #         1
    #        / \
    #       2   3
    #        \   \
    #         5   4
    # expected output: [1,3,4]
    root = Node(1)
    root.left = Node(2, None, Node(5))
    root.right = Node(3, None, Node(4))
    assert right_side_view(root) == [1, 3, 4]

    # input: [1,null,3]
    #         1 
    #          \
    #           3
    # expected output: [1,3]
    root = Node(1, None, Node(3))
    assert right_side_view(root) == [1,3]

    # input: [1,2,3,null,5,null,4,7,null,null,null]
    #         1
    #        / \
    #       2   3
    #        \   \
    #         5   4
    #         /
    #        7
    # expected output: [1,3,4,7]
    root = Node(1)
    root.left = Node(2, None, Node(5, Node(7)))
    root.right = Node(3, None, Node(4))
    assert right_side_view(root) == [1,3,4,7]

    print('All passed!')