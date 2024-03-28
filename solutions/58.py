"""
Problem Link: https://leetcode.com/problems/length-of-last-word/

Time complexity: O(n) due to the .split() operation on the string. The .split() method goes through each character of the string.
Space complexity: O(n) due to storing of the split words.
"""

def length_last_word(s):
    if not s.strip():
        return 0
    s = s.split()
    last_word_ind = len(s) - 1
    last_word  = s[last_word_ind]
    return len(last_word)

if __name__ == "__main__":
    assert length_last_word("Hello World") == 5
    assert length_last_word("   fly me   to   the moon  ") == 4
    assert length_last_word("         Hello") == 5
    assert length_last_word("Wonderful") == 9
    assert length_last_word("") == 0
    assert length_last_word("    ") == 0

    print("All test cases passed!")
