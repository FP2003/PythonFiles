def canConstruct(ransomNote: str, magazine: str) -> bool:
    # Iterate through each character in the ransomNote
    for i in ransomNote:
        # Check if the character exists in the magazine
        if i in magazine:
            # Remove one occurrence of the character from both ransomNote and magazine
            ransomNote = ransomNote.replace(i, '', 1)
            magazine = magazine.replace(i, '', 1)
            # If ransomNote becomes empty, return True indicating it can be constructed
            if len(ransomNote) == 0:
                return True
        # If the character doesn't exist in magazine, return False
        else:
            return False
    # If the loop completes without returning True, return True
    return True

print(canConstruct("aa", "ab"))