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
