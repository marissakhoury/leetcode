"""
Problem Link: https://leetcode.com/problems/sqrtx/

Approach: 
- Binary search algorithm to find square root
- Search for the square root in the range 0 to x
- Repeatedly narrow down the search interval based on whether the square of the midpoint is greater than, less than, or equal to x 

Time Complexity: O(log n) where n is the value of input x. Each iteration, we half the search space 
Space Complexity: O(1), constant space not depending on input size x. 
"""
def sqrt_x(x):
    left, right = 0, x
    res = 0
    while left <= right:
        m = left + (right - left) // 2
        if m**2 > x:
            right = m - 1
        elif m**2 < x:
            left = m + 1
            res = m
        else:
            return m 
    return res

if __name__ == "__main__":
    assert sqrt_x(25) == 5
    assert sqrt_x(4) == 2
    assert sqrt_x(8) == 2
    assert sqrt_x(0) == 0
    print('All passed!')