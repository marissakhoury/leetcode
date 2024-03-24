"""
Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def merge_two_lists(l1, l2):
    dummy = Node()
    tail = dummy
    
    while l1 and l2: 
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next # update the tail pointer

    # handle any remaining elements 
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next

# Test Merge
l1 = Node(1, Node(2, Node(4)))
l2 = Node(1, Node(3, Node(4)))

merged_list = merge_two_lists(l1, l2)
current = merged_list

while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next