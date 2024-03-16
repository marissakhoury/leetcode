"""
Problem Link: https://leetcode.com/problems/rotate-array/

Naive Approach: 
- Initialize result array
- Shift elements from position `i` to position (`i + k`) % (`len(nums)`)

Time Complexity: O(n).
Space Complexity: O(n). This approach initializes a result array of the same size as input array to store the rotated elements. So, the space complexity is proportional to the size of the input.

Better Approach:
e.g. given [1, 2, 3, 4, 5], k = 2
1) Reverse entire input array --> [5, 4, 3, 2, 1]
2) Reverse first `k` elements of reversed array --> [4, 5, 3, 2, 1]
3) Reverse remaining elements of array --> [4, 5, 1, 2, 3]

Time Complexity: O(n).
Space Complexity: O(1). Constant space complexity. 
"""
def naive_rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    """
    result = [None] * len(nums) # initialize result array with placeholder values
    for i, num in enumerate(nums):
        new_idx = (i + k) % (len(nums))
        result[new_idx] = num
    return result

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    """
    k = k % len(nums)
    left, right = 0, len(nums) - 1

    # first reversal
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1

    # second reversal: reversing first k elements of array
    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1

    # final reversal: reverse remaining portion of array 
    left, right = k, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1
    
    return nums

if __name__ == "__main__":
    # Test case 1
    original_nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    assert naive_rotate(original_nums[:], k) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate(original_nums[:], k) == [5, 6, 7, 1, 2, 3, 4]
    print("Passed!")

    # Test case 2
    original_nums = [-1, -100, 3, 99]
    k = 2    
    assert naive_rotate(original_nums[:], k) == [3, 99, -1, -100]
    assert rotate(original_nums[:], k) == [3, 99, -1, -100]
    print("Passed!")
