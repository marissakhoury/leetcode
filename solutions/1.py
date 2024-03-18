"""
Problem Link: https://leetcode.com/problems/two-sum/

Brute Force Solution: Sum all possible combinations of elements and see if any add up to the target sum

Time Complexity: O(n^2) due to the nested loop (compares every possible pair of numbers in the array)
Space Complexity: O(1), constant space. 

Method 1: Using Sorting and Two Pointers
- First sort array from smallest to largest
- Two pointers, left (start at 0) and right (start at len(nums)-1)
- Try to sum left and right elements of sorted array
    - If the sum of left and right is greater than target, decrement right pointer
    - If the sum of left and right is less than target, increment left pointer 

Time Complexity: O(n log n) due to sorting being the most significant operation.
Space Complexity: O(n) due to the need to store a copy of the original array for sorting.

Method 2: Using Hashing
- Initialize nums_dict
- Iterate through array
- Check complement (`val`): 
    - For each current number, calculate its complement (the number needed to add up to the target). Then check if this complement exists in the dictionary.
    - Found Pair: If complement is found, means a pair of numbers that add up to the target has been identified. Stop and return indices of current number and complement as found in nums_dict.
    - If no complement is found, the current number and its index are stored in the dictionary for future reference.

Time Complexity: O(n). Iterates through list once. Note: Hashtable lookups are O(1) on average, so overall time complexity is linear with respect to number of elements n. 
Space Complexity: O(n). In the worst case (where no 2 numbers sum to target until very end or not at all), the method ends up storing every number in the dictionary. So space complexity is linear with respect to number of elements n. 

Summary (Method 2):
1. Utilizes a dictionary for fast lookups of complements! O(1) lookup in dict! 
2. Iterates through the list once, making it time-efficient.
3. Stores at most every number and its index in the dictionary, leading to a linear space requirement.
"""

def brute_force_two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

def sorting_two_sum(nums, target):
    """
    Using sorting.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    sorted_nums = sorted(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = sorted_nums[left] + sorted_nums[right]
        if current_sum > target:
            right -= 1
        if current_sum < target:
            left += 1
        else: # current_sum == target
            num1, num2 = sorted_nums[left], sorted_nums[right]
            idx1, idx2 = nums.index(num1), nums.index(num2) if num1 != num2 else nums.index(num2, nums.index(num1) + 1) # handles case where num1 and num2 are the same (e.g. [3,3], target=6) since index function returns the first match it finds
            return (idx1, idx2)

def hashing_two_sum(nums, target):
    """
    Using hashing.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}
    for i in range(len(nums)): 
        val = target - nums[i]
        if val in nums_dict:
            return (i, nums_dict[val])
        nums_dict[nums[i]] = i
    return None

test_cases = [
    ([2, 7, 11, 15], 9, (0, 1)),  
    ([3, 2, 4], 6, (1, 2)),       
    ([3, 3], 6, (0, 1)),      
    ([-1, -2, -3, -4, -5], -8, (2, 4)),  
    ([1, 2, 3, 4, 5, 6], 11, (4, 5)),    
]

# Brute Force Two Sum
for nums, target, expected in test_cases:
    assert brute_force_two_sum(nums, target) == expected, f"brute_force_two_sum failed on input {nums} with target {target}"

# Hashing Two Sum
for nums, target, expected in test_cases:
    result = hashing_two_sum(nums, target)
    assert (nums[result[0]] + nums[result[1]] == target), f"hashing_two_sum failed on input {nums} with target {target}"

print("All tests passed!")
