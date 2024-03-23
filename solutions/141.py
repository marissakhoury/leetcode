"""
Problem Link: https://leetcode.com/problems/linked-list-cycle/

Approach 1: nodes_seen set 
- Need to maintain hashset of visited nodes
Time Complexity: O(n)
Memory Complexity: O(n) since using additional datastructure

Approach 2: Floyd's Tortoise and Hare 
- Two pointers, fast and slow (initially both start at head)
    - slow pointer shifts by 1 
    - fast pointer shifts by 2
If there is no cycle: fast pointer will always be ahead of slow pointer
BUT if there is a cycle: the fast and slow pointer will meet again at the exact same position --> there is a cycle 

Time Complexity: O(n)
Memory Complexity: O(1)
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle_hashset(head):
    nodes_seen = set()
    curr = head
    while curr: # while current is not none
        if curr in nodes_seen:
            return True
        nodes_seen.add(curr)
        curr = curr.next
    return False 

def has_cycle_floyd(head):
    slow, fast = head, head

    while fast and fast.next: # need to check while fast and fast.next are not null since fast is moving 2 slots each iteration
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # if slow ever reaches fast, we know there is a cycle 
            return True
    # returning False outside of the loop because if we get here, we know fast reaches null and therefore no cycle exists 
    return False

def test_has_cycle_hashset():
    head1 = Node(1, Node(2, Node(3)))
    assert not has_cycle_hashset(head1)

    head2 = Node(1, Node(2, Node(3)))
    head2.next.next.next = head2
    assert has_cycle_hashset(head2)

    head3 = None
    assert not has_cycle_hashset(head3)

    head4 = Node(1)
    assert not has_cycle_hashset(head4)

    head5 = Node(1)
    head5.next = head5
    assert has_cycle_hashset(head5)

    print("All HashSet tests passed!")

def test_has_cycle_floyd():
    head1 = Node(1, Node(2, Node(3)))
    assert not has_cycle_floyd(head1)

    head2 = Node(1, Node(2, Node(3)))
    head2.next.next.next = head2
    assert has_cycle_floyd(head2)

    head3 = None
    assert not has_cycle_floyd(head3)

    head4 = Node(1)
    assert not has_cycle_floyd(head4)

    head5 = Node(1)
    head5.next = head5
    assert has_cycle_floyd(head5)

    print("All Floyd's cycle detection tests passed!")

if __name__ == "__main__":
    test_has_cycle_hashset()
    test_has_cycle_floyd()

