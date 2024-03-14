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
    assert majority_element(nums1) == 3
    
    nums2 = [2,2,1,1,1,2,2]
    assert majority_element(nums2) == 2
    
    print("Passed!")