"""
Problem Link: https://leetcode.com/problems/3sum/

Approach: 
1. Sort input array
2. Use each number in the input array as a possible first value (iterate through index and value)
3. Assign left and right pointers and use two pointer solution for the remaining portion of the array (basically solve 2sum)

Time Complexity: O(nlogn) from sorting + O(n^2) --> O(n^2)
"""

def three_sum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]: # means duplicate value so we want to skip and continue to next iteration of loop
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right: 
            curr_sum = a + nums[left] + nums[right]
            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                # need to update the left pointer only
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res

if __name__ == "__main__":
    assert three_sum([-1,0,1,2,-1,-4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0,0,0]) == [[0, 0, 0]]
    assert three_sum([0,1,1]) == []
    print('All passed!')