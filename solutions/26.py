"""
Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/ 

Intuition/Approach:
- First value in the array will stay in the first position of the output array (since first element must be unique)
- Two pointers are needed:
    - `i` pointer scans the array from the second element since the first element is always unique
    - `k` pointer tracks where to put the next unique value (this pointer will also be the output of the function)
- Both `i` and `k` pointers begin at position 1, going through the length of the `nums` array.
- Check the current element (at position `i`) against the previous element (position `i-1`).
    - If `nums[i]` does not equal `nums[i-1]`, then set `nums[k]` to be `nums[i]` and increment `k` by 1.
- By the end of the iteration, the first `k` elements in `nums` are the unique elements, and `k` equals the total count of these unique elements

Time Complexity: O(n), where `n` is the number of elements in `nums`
Space Complexity: O(1), modifications done in-place
"""

def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 1
    i = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = remove_duplicates(nums)
    assert nums[:5] == [0,1,2,3,4]
    assert k == 5
    print("Passed!")
