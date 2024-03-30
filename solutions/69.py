"""
Problem Link: https://leetcode.com/problems/sqrtx/
"""
def sqrt_x(x):
    left, right = 0, x
    res = 0
    while left <= right:
        m = left + ((right - 1) // 2)
        if m**2 > x:
            right = m - 1
        elif m**2 < x:
            left = m + 1
            res = m
        else:
            return m 
    return res

assert sqrt_x(25) == 5
assert sqrt_x(4) == 2
assert sqrt_x(8) == 2
print('All passed!')