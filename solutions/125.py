"""
Problem Link: https://leetcode.com/problems/valid-palindrome/

Naive Approach:
- Instantiate new empty string `new_str`
- Iterate through each `char` in `s`, check if `char` is an alphanumeric char (using built in python function `.isalnum()`), apply `.lower()` to character, append it to `new_str`
- Return new_str == new_str[::-1]

Time Complexity: O(n).
Space Complexity: O(n). Allocating extra memory for new_str and uses extra memory for the string reversal `new_str[::-1]`

Better Approach (Using 2 pointers): 
- No reversal done, instead use left and right pointers to check if chars are the same
- added function alpha_num to check if char is an alphanumeric character

Time Complexity: O(n).
Space Complexity: O(1). 
"""
def naive_is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    new_str = ""
    for char in s:
        if char.isalnum():
            new_str += char.lower()
    return new_str == new_str[::-1]

def alpha_num(char):
    """
    Function to determine if char is an ASCII value.
    Returns true if char is between A - Z , a - z, or 0 - 9
    """
    return (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))

def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not alpha_num(s[left]):
            left += 1
        while right > left and not alpha_num(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    assert naive_is_palindrome(s[:]) == True
    assert is_palindrome(s[:]) == True
    print('Passed!')

    s = "race a car"
    assert naive_is_palindrome(s[:]) == False
    assert is_palindrome(s[:]) == False
    print('Passed!')

    s = " "
    assert naive_is_palindrome(s[:]) == True
    assert is_palindrome(s[:]) == True
    print('Passed!')

    s = " ., "
    assert naive_is_palindrome(s[:]) == True
    assert is_palindrome(s[:]) == True
    print('Passed!')
