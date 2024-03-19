"""
Problem Link: https://leetcode.com/problems/valid-anagram
"""
def is_anagram(s, t):
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
    
print(is_anagram('mad', 'adm'))
print(is_anagram('mmaamm', 'aammm'))