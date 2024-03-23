"""
Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum > target:
            right -=1
        elif curr_sum < target:
            left += 1
        else:
            return [left+1, right+1]

nums = [1, 3, 4, 5, 7, 10, 11]
target = 9
print(two_sum(nums, target))