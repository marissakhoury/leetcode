"""
Problem Link: https://leetcode.com/problems/merge-sorted-array/

Intuition:
- Traverse in reverse order 
- nums1 has enough space at the end to accommodate all elements of nums2

Approach
1. Initialize pointers
- last is set to the last index of nums1 (m + n - 1), where the merged elements will be placed
- the given arrays are traversed in reverse, starting from the ends of their respective meaningful elements (m-1 for nums1 and n-1 for nums2)
2. Merge in Reverse
- compare the elements at the current positions of nums1 and nums2
- place the larger element at the last index of nums1
- decrement last and the index (m or n) of the array from which the element was taken
3. Handle leftover elements
- there may be some elements left in nums2 (if nums1's elements were larger thus placed first)
- leftovers are placed in remaining positions of nums1

Time Complexity: O(m + n), where m is the number of elements in nums1, and n is the number of elements in nums2. Each element in both arrays is visited at most once.
Space Complexity: O(1), no additional space is required, as the merge is done in-place.
"""

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    last = m + n - 1
    # merge in reverse order
    while m > 0 and n > 0:
        if (nums1[m - 1] > nums2[n - 1]):  # comparing last real value of nums1 and last value of nums2
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # fill nums1 with leftover nums2 elements
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1 == [1,2,2,3,5,6]
    print("Passed!")