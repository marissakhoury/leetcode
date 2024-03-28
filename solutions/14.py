"""
Problem Link: https://leetcode.com/problems/longest-common-prefix/
"""

def longest_common_prefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]: # if i == len(s) -> means we are out of bounds, return res
                return res
        res += strs[0][i]
    return res


if __name__ == "__main__":
    assert longest_common_prefix(["flower","flow","flight"]) == "fl"
    assert longest_common_prefix(["dog","racecar","car"]) == ""
    print('All passed!')