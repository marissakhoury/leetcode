""""
Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

Brute Force Approach:
Time Complexity: O(k * n)

Time Complexity: O(n * log k) logk is the number of times we are repeating this n step 
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
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

def merge_k_lists(lists):
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged.append(merge_two_lists(l1, l2))

        lists = merged

    return lists[0]

def build_linked_list(arr):
    dummy = Node()
    current = dummy
    for val in arr:
        current.next = Node(val)
        current = current.next
    return dummy.next

def linked_list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

if __name__ == "__main__":
    lists = [build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert linked_list_to_array(merge_k_lists(lists)) == expected
    
    lists = [build_linked_list([1, 2, 2]), build_linked_list([1, 1, 2])]
    expected = [1, 1, 1, 2, 2, 2]
    assert linked_list_to_array(merge_k_lists(lists)) == expected
    
    print("All test cases passed!")
