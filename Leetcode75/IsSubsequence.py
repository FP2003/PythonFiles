def isSubsequence(s: str, t: str) -> bool:
    # Initialize index pointer for string s
    i = 0
    # If's is empty, it's always a subsequence
    if not s:
        return True
    # Iterate through each character in string t
    for char in t:
        # If the current character matches the character in s at index i
        if char == s[i]:
            # Move to the next character in s
            i += 1
            # If all characters in s are found in t
            if i == len(s):
                return True
    # If not all characters in s are found in t
    return False

print(isSubsequence("abc", "ahbgdc"))