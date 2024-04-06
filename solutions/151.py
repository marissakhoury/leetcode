"""
Problem Link: https://leetcode.com/problems/reverse-words-in-a-string/
"""

def reverse_words_in_string(s):
    s = str.split(s)
    s = s[::-1]
    s = ' '.join(s)
    return s

import collections
def reverse_words_in_string_2(s):
    string_builder = collections.deque()
    start = -1
    i = 0

    while i < len(s):
        if s[i] != " ":
            start = i
            while i < len(s) and s[i] != " ":
                i += 1
            string_builder.appendleft(s[start: i])
            i -= 1
        i += 1
    return " ".join(string_builder)

if __name__ == "__main__":
    assert reverse_words_in_string_2("hello") == "hello"
    assert reverse_words_in_string_2("hello world") == "world hello"
    assert reverse_words_in_string_2("  hello world  ") == "world hello"
    assert reverse_words_in_string_2("hello   world") == "world hello"
    assert reverse_words_in_string_2("  hello   world   from   python  ") == "python from world hello"
    assert reverse_words_in_string_2("") == ""
    assert reverse_words_in_string_2("     ") == ""
    print("All tests passed!")