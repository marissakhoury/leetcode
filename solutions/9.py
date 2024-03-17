"""
Problem Link: https://leetcode.com/problems/palindrome-number/

Naive Solution:
- Cast int to str
- Use two pointer technique to verify if it is a palindrome

Time Complexity: O(n), where n is the number of digits in the number. 
Space Complexity: O(n), because we convert the number to a string which takes up space proportional to the number of digits in the number.

Better Solution (Using math operations):
1. Handle Negative Numbers: Since negative numbers can't be palindromes ("-" sign), return False.
2. Find the Divisor: Initialize a divisor to help extract the first digit of the number.
 - Start with a divisor of 1 and keep multiplying it by 10 until it's just less than or equal to the number. 
 - Divisor now represents the place value of the first digit of the number. (e.g. x = 12345, divisor will be 10000 after this step)
3. Compare Digits:
- Extract the Last Digit: (e.g., 12345 % 10 = 5).
- Extract the First Digit: Get it by dividing the number by the divisor determined earlier (e.g., 12345 // 10000 = 1).
- If the first and last digits don't match, the number cannot be a palindrome, so we return False.
4. Remove Checked Digits: After comparing the first and last digits, we need to remove them from the number to check the next pair of digits. 
- Remove the first digit and then divide by 10 again to remove the last digit (e.g., (12345 % 10000) // 10 = 234).
5. Update the Divisor: Divide our divisor by 100 to update its value.

Time Complexity: O(log n), where n is the value of the number. The time complexity arises from the fact that the number of operations needed scales with the number of digits in the number, which grows logarithmically with n.
Space Complexity: O(1), because this approach only uses a fixed amount of extra space regardless of the input size.
"""

def naive_is_palindrome(x):
    """
    Checks if number is a palindrome by converting it to a string and using 2 pointers. 
    :type x: int
    :rtype: bool
    """
    str_x = str(x)
    left, right = 0, len(str_x) - 1
    while left < right:
        if str_x[left] != str_x[right]:
            return False
        left += 1
        right -=1
    return True

def is_palindrome(x):
    """
    Checks if a number is a palindrome without converting it to a string, by comparing digits from both ends using mathematical operations.
    :type x: int
    :rtype: bool
    """
    # negative numbers are not palindromes
    if x < 0:
        return False
    # find the divisor to extract the leading digit
    div = 1
    while x >= 10 * div:
        div *= 10
    while x:
        right_digit = x % 10
        left_digit = x // div
        if left_digit != right_digit:
            return False
        # chop off left digit with x = x % 10
        # chop off right digit with x // 10
        x = (x % div) // 10
        # update divisor to reflect the removal of 2 digits
        div = div / 100
    return True

if __name__ == "__main__":
    test_cases = [121, -121, 123, 1221, 0, 10, 111, 2222, 12321, -12321]
    expected_results = [True, False, False, True, True, False, True, True, True, False]

    for i, test_case in enumerate(test_cases):
        assert naive_is_palindrome(test_case) == expected_results[i]
        assert is_palindrome(test_case) == expected_results[i]
    
    print('All test cases passed!')
