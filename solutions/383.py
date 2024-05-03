"""
Problem Statement: https://leetcode.com/problems/ransom-note/
"""

def can_construct(ransom_note, magazine):
    magazine_chars = {}
    if len(ransom_note) > len(magazine):
        return False
    
    # build up frequency dict for magazine
    for i in range(len(magazine)):
        magazine_chars[magazine[i]] = 1 + magazine_chars.get(magazine[i], 0)

    # check each char in ransom note
    for i in range(len(ransom_note)):
        
        if ransom_note[i] in magazine_chars and magazine_chars[ransom_note[i]] >= 1: 
            magazine_chars[ransom_note[i]] -= 1 # decrement count for that char in magazine_chars
        else:
            return False
    return True


if __name__ == "__main__":
    # Test Case 1: Magazine has more characters than needed
    assert can_construct("aa", "aab") == True

    # Test Case 2: Not enough characters in magazine
    assert can_construct("aaa", "aab") == False

    # Test Case 3: Empty ransom note should always return True
    assert can_construct("", "anything") == True

    # Test Case 4: Magazine is empty but ransom note is not
    assert can_construct("anything", "") == False

    # Test Case 5: Characters are the same
    assert can_construct("thesame", "samethe") == True

    # Test Case 6: Both empty
    assert can_construct("", "") == True

    # Test Case 7: Random larger case
    assert can_construct("thequickbrownfox", "thequickbrownfoxjumps") == True

    # Test Case 8: Repetitive chars
    assert can_construct("give me moneyyy", "give me moneyy") == False

    print("All tests passed!")