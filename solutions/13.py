"""
Problem Link: https://leetcode.com/problems/roman-to-integer/

Time Complexity: O(n). Iterates once through the input string of length n, performing constant time operations for each character.
Space Complexity: O(1). The space used does not grow with the size of the input. Constant space complexity. 
"""

def roman_to_int(s):
    """
    Given a roman numeral, convert it to an integer.
    Largest to smallest: add them up
    smaller before larger: subtract smaller 
    """
    rom_to_int = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
    res = 0
    for i in range(len(s)):
        # check if i+1 is in bounds and if value at i+1 is greater than value at i
        if i + 1 < len(s) and rom_to_int[s[i+1]] > rom_to_int[s[i]]:
            res -= rom_to_int[s[i]] # subtract smaller
        else:
            res += rom_to_int[s[i]]
    return res

if __name__ == "__main__":
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    print("All tests passed!")

