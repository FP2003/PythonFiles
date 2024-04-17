def lengthOfLastWord(s: str) -> int:
    # Initialize length counter
    length = 0
    # Start from the end of the string
    i = len(s) - 1
    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
    # Count the length of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    # Return the length of the last word
    return length

print(lengthOfLastWord('Hello World'))