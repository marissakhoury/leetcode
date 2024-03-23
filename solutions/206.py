""""
Problem Link: https://leetcode.com/problems/reverse-linked-list/

Solution 1: Iterative approach with 2 pointers
Time Complexity: O(n)
Space Complexity: O(1), in-place operation, not using any additional data structures.

Solution 2: Recursive approach
Time Complexity: O(n)
Space Complexity: O(n)

"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def reverse_recursive(head):
    if not head:
        return None
    new_head = head
    if head.next:
        new_head = reverse_recursive(head.next)
        head.next.next = head
    head.next = None
    return new_head

def reverse_recursive(head):
    def reverse(curr, prev):
        if curr is None:
            return prev
        else:
            temp = curr.next
            curr.next = prev
            return reverse(temp, curr)
    return reverse(head, None)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def test_reverse_functions():
    print("\nTest 1: Empty")
    head = None
    print("Original list:")
    print_list(head)
    print("Iterative Reverse:")
    print_list(reverse_iterative(head))
    print("Recursive Reverse:")
    print_list(reverse_recursive(head))

    print("\nTest 2: Single element")
    head = Node(1)
    print("Original list:")
    print_list(head)
    print("Iterative Reverse:")
    print_list(reverse_iterative(head))
    head = Node(1)  # recreate since it's modified by the previous function
    print("Recursive Reverse:")
    print_list(reverse_recursive(head))

    print("\nTest 3: Multiple elements")
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print("Original list:")
    print_list(head)
    print("Iterative Reverse:")
    print_list(reverse_iterative(head))
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))  
    print("Recursive Reverse:")
    print_list(reverse_recursive(head))

if __name__ == "__main__":
    test_reverse_functions()