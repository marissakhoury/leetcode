"""
Problem Link: https://leetcode.com/problems/reverse-words-in-a-string/
"""

def reverse_words_in_string(s):
    s = str.split(s)
    s = s[::-1]
    s = ' '.join(s)
    return s


if __name__ == "__main__":
    assert reverse_words_in_string("hello  my name is marissa ") == "marissa is name my hello"
    print('passed!')