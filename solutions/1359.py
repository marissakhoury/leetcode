"""
Problem Link: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
"""

def count_orders(n):
    slots = 2 * n
    output = 1
    while slots > 0:
        valid_choices = slots * (slots - 1) // 2
        output *= valid_choices
        slots -= 2
    return output % (10 ** 9 + 7)

if __name__ == "__main__":
    assert count_orders(1) == 1
    assert count_orders(2) == 6
    assert count_orders(3) == 90
    assert count_orders(4) == 2520
    
    print("All tests passed!")