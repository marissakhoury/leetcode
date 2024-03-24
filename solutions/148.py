"""
Problem Statement: https://leetcode.com/problems/sort-list/

Approach: Recursive Merge Sort
- Split list in half/ divide and conquer

Time Complexity: O(nlogn), merge sort runs in nlogn time
Memory Complexity: O(logn), since we are doing it recursively
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_mid(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(list1, list2):
    dummy = Node()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return dummy.next 

def sort_list(head):
    # base case
    if not head or not head.next:
        return head
    
    # split the list into two halves
    left = head
    right = get_mid(head) # calls get_mid helper function
    temp = right.next
    right.next = None
    right = temp

    left = sort_list(left)
    right = sort_list(right)
    
    # calls merge helper function
    return merge(left, right)