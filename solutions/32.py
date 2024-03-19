"""
Problem Link: https://leetcode.com/problems/longest-valid-parentheses/

Approach (Two Pass Solution: Scan from both directions to catch all valid substrings)
- Maintain a left count "("
- Maintain a right count ")"
- When left == right: we know we have "()", update longest to max(longest, left + right)


Time Complexity: O(N) + O(N) = O(2N) --> O(N).
Space Complexity: O(1), constant space since we do not define any additional data structures. 
"""
def longest_valid_paren(s: str) -> int:
    """
    Return length of longest valid paren substring.
    Scans from both directions.
    """
    longest = 0
    left = 0
    right = 0
    i = 0
    # first pass: left to right
    while i < len(s):
        if s[i] == "(":
            left += 1
        else: # s[i] == ")"
            right += 1

        if left == right:
            longest = max(longest, left + right)
        elif right > left: # means no longer valid, reset left and right counts
            left, right = 0, 0  
        i += 1

    # reset left and right counts to 0 and i to the last char of s
    left, right = 0, 0
    i = len(s) - 1
    
    # second pass: right to left 
    while i >= 0:
        if s[i] == "(":
            left += 1
        else:
            right += 1
        
        if left == right:
            longest = max(longest, left + right)
        elif left > right:
            left, right = 0, 0
        i -= 1
    return longest

if __name__ == "__main__":
    assert longest_valid_paren(")()())") == 4, "Test case 1 failed: Expected 4"
    assert longest_valid_paren("(()") == 2, "Test case 2 failed: Expected 2"
    assert longest_valid_paren("") == 0, "Test case 3 failed: Expected 0"
    print("All tests passed!")
