def wordPattern(pattern: str, s: str) -> bool:
    # Split the string s into words
    s = s.split(' ')

    # Check if the lengths of pattern and s are equal
    if len(pattern) != len(s):
        return False
    
    # Dictionaries to map characters to words and vice versa
    wordToChar = {}
    charToWord = {}

    # Iterate through pattern and s simultaneously using zip
    for x, y in zip(pattern, s):
        # If the character is already mapped to a word and it's not the current word, return False
        if x in charToWord and charToWord[x] != y:
            return False
        # If the word is already mapped to a character and it's not the current character, return False
        if y in wordToChar and wordToChar[y] != x:
            return False
        # Map the character to the word and the word to the character
        charToWord[x] = y
        wordToChar[y] = x
    
    # If no inconsistencies found, return True
    return True

print(wordPattern("abba", "dog cat cat dog"))