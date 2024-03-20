"""
Problem Link: https://leetcode.com/problems/valid-parentheses/

Approach:
- Need to start with an open paren of any kind (can't start with closing paren)
- Once we start with an open paren, we can add many open paren as we want, as long as they are closed eventually

1. Stack for open parentheses: use a stack to manage opening parens to allow us to check if most recent opening paren matches the current closing one
2. Hashmap for parentheses matching {closed paren : open paren}

Time Complexity: O(n). Scanning array once.
Space Complexity: O(n). Since we have a stack that could be as big as n in the worst case (if al the characters are open parens for example)
"""
def is_valid(s):
    closed_to_open = { ")": "(", "]" : "[", "}" : "{" } # closing paren (key) : open paren (value)
    stack = []
    for char in s:
        if char in closed_to_open: # means char is a closing paren 
            if stack and stack[-1] == closed_to_open[char]: # if stack is not empty and last element in stack is the corresponding open paren
                stack.pop() # good, pop it off
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False

if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("(((())))") == True
    assert is_valid("()[") == False
    
    print("All test cases passed!")