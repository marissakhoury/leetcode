"""
Problem Link: https://leetcode.com/problems/majority-element/

Naive Approach: 
- Implement as if we were finding the "most common" element in the array
- Use hashmap/dict to map element to number of occurrences

Time Complexity: O(n).
Space Complexity: O(n). Since we are using a data structure: a hashmap. Worst case, if all elements in nums are unique, dict would have an entry for each element --> memory complexity of O(n). 

Better Approach, "Boyer-Moore Voting Algorithm":
- Problem statement says there will always be an element that occurs in more than half of the array's contents
- This algorithm operates under the above assumption (that a majority element always exists)
- Iteration:
    - if `count` is 0, the current number `num` is chosen as the new `candidate` for the majority element 
    (this step resets the candidate whenever `count` drops to 0, meaning that up to this point there is no majority element in the scanned portion of the array)
    - if current number `num` is the same as the current `candidate`, INCREMENT `count` by 1
    - if `num` is NOT the same as `candidate`, DECREMENT `count` by 1 (represents a vote against current candidate)

Time Complexity: O(n).
Space Complexity: O(1). 
"""

def naive_majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    occurrences_dict = {}
    for num in nums:
        if num in occurrences_dict:
            occurrences_dict[num] += 1
        else:
            occurrences_dict[num] = 1
    return max(occurrences_dict, key=occurrences_dict.get)


def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

if __name__ == "__main__":
    nums1 = [3,2,3]
    assert naive_majority_element(nums1) == 3
    assert majority_element(nums1) == 3
    print("Passed!")

    nums2 = [2,2,1,1,1,2,2]
    assert naive_majority_element(nums2) == 2
    assert majority_element(nums2) == 2
    print("Passed!")