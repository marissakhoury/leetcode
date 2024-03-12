"""
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Approach:
1. Initialize pointer `i = 0` (indicating next position for a valid element)
2. Iterate through array (`for num in nums`)
- Place `num` at `nums[i]` if:
    - `i < 2` (means we are at the start of the list and can safely keep first two elements without any further checks) OR 
    - `num > nums[i-2]` (means current number is NOT a duplicate of the last two numbers)
- Increment `i` if a number is placed
3. Return `i` as new length of array

Time Complexity: O(n), each element in nums is considered at most once. 
Space Complexity: O(1), performed in-place, does not use any additional space.
"""

def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0 
    for num in nums:
        if i < 2 or num > nums[i-2]:
            nums[i] = num
            i += 1
    return i


if __name__ == "__main__":
    # Example 1
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = remove_duplicates(nums)
    assert k == 7, "k should be 7"
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3], "Array contents incorrect"

    # Example 2
    nums = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates(nums)
    assert k == 5, "k should be 5"
    assert nums[:k] == [1, 1, 2, 2, 3], "Array contents incorrect"

    print("Passed!")

