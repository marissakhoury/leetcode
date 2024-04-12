"""
Breadth-First Search Algorithm (BFS) for Binary Trees
- Uses a queue to keep track of the nodes to be visited and processes each node level by level
- Queue Processing (while there are nodes in the queue:)
    - remove current node from the front of queue pop(0)
    - add the current node's value to the result list
    - check if the current node has left and right children and add them to the queue 
    - return res (contains the values of nodes visited in BFS order)
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if not root:
        return [] # return empty list if root is None
    res = []
    q = [root]
    while q:
        # pop off curr node from left
        node = q.pop(0)
        # add curr node val to res
        res.append(node.val)
        # process children
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

if __name__ == "__main__":
    # Test case 1: Empty tree
    assert bfs(None) == []

    # Test case 2: Single node
    root = Node(1)
    assert bfs(root) == [1]

    # Test case 3: Full binary tree
    root = Node(1, Node(2), Node(3))
    assert bfs(root) == [1, 2, 3]

    # Test case 4: Imbalanced tree
    root = Node(1, Node(2, Node(4)), Node(3))
    assert bfs(root) == [1, 2, 3, 4]

    # Test case 5: Larger binary tree
    root = Node(1, Node(2, Node(4, Node(6)), Node(5)), Node(3))
    assert bfs(root) == [1, 2, 3, 4, 5, 6]

    print("All tests passed!")