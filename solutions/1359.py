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