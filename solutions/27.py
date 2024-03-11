"""
Problem Link: https://leetcode.com/problems/remove-element/

Approach 1: Naive Remove Element
1. Initialize k pointer
   - k starts at 0. This index will represent the next position in the array where a non-val element should be placed
2. Iterate through array
   - Use index i to loop through, comparing nums[i] to val
   - If nums[i] != val, place nums[i] at kth position and increment k
   - Elements beyond nums[k:] disregarded

Time Complexity: O(n), each element in nums is considered at most once. 
Space Complexity: O(1), performed in-place.

Approach 2: Front/Rear Swap with Counter
1. Initialize front/rear pointers and counter (k)
   - front starts at the beginning of nums, rear at the end of array
   - k starts at 0
2. Compare and Swap
   - While front is less than rear, compare the elements at these positions with val
   - If front finds val, and rear finds a non-val, swap them. This action moves val elements towards the end (and non-val elements towards the front).
   - After a successful swap or if rear points to val, decrement rear
   - If front points to a non-val element, increment both front and k
3. Final Adjustment
   - After the loop completes, check the element at the front position. If it's not equal to val, increment k once more to include this last element in the count.

Unlike the naive approach, this method maintains all original values of the array, with values equal to val moved to the end.
- Time Complexity: O(n), as each element is considered at most once.
- Space Complexity: O(1), performed in-place.
"""

def naive_remove_element(nums, val):
    """
    Moves all values equal to val to the back, disregards values nums[k:]
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        i += 1
    return k


def remove_element(nums, val):
    """
    Moves all values equal to val to the back, maintains all values.
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k, front = 0, 0
    rear = len(nums) - 1
    while front < rear:
        # check front
        if nums[front] != val:
            # move on
            front += 1
            k += 1
        else:
            # front needs to be swapped
            if nums[rear] == val:  # check if rear can be swapped
                rear -= 1
            else:
                # swap
                temp = nums[front]
                nums[front] = nums[rear]
                nums[rear] = temp
                k += 1
                front += 1
                rear -= 1
    # final check
    if nums[front] != val:
        k += 1
    return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    k = naive_remove_element(nums, val)
    assert k == 2

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = naive_remove_element(nums, val)
    assert k == 5


    nums = [3, 2, 2, 3]
    val = 3
    k = remove_element(nums, val)
    assert k == 2

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = remove_element(nums, val)
    assert k == 5
    print("Passed!")
