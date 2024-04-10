class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    res = []
    q = [root]
    while q:
        # pop off curr node
        node = q.pop(0)
        # add curr node val to res
        res.append(node.val)
        # process children (add children to q)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res
