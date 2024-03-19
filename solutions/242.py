"""
Problem Link: https://leetcode.com/problems/valid-anagram

Hashmap solution:
- Create dictionaries for letters in s and letters in t
- Check to see if they are the same length first: if not, then they are not palindromes --> return False immediately
- Hashmap function .get(x, 0) is important to use (default to 0 if key does not exist in hashmap; avoids keyerrors)
- Finally, iterate through hashmap and see if counts in both hashmaps are the same 

Time Complexity: O(s) + O(t) = O(s+t) --> O(n)
Space Complexity: O(s) + O(t) = O(s+t) --> O(n)

Sorting solution:
- Sort characters to see if they are the exact same string

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
def is_anagram(s, t):
    """
    Hashmap solution
    """
    letters_s, letters_t = {}, {}
    if len(s) != len(t):
        return False
    # build up the dicts 
    for i in range(len(s)):
        letters_s[s[i]] = 1 + letters_s.get(s[i], 0)
        letters_t[t[i]] = 1 + letters_t.get(t[i], 0)
    # iterate through dict and compare results
    for c in letters_s:
        if letters_s[c] != letters_t.get(c, 0):
            return False
    return True

def is_anagram2(s, t):
    """
    Sorted solution.
    """
    return sorted(s) == sorted(t)
    
if __name__ == "__main__":
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "bello") == False
    
    assert is_anagram2("listen", "silent") == True
    assert is_anagram2("hello", "bello") == False
    print("All tests passed!")