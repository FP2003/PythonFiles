def reverseWords(s: str) -> str:
    # Split the input string into words
    res = s.split()
    # Join the words back into a string
    clean = ' '.join(res)
    # Split the string again to get individual words
    newS = clean.split(' ')
    # Reverse the order of words
    rev = newS[::-1]
    # Initialize an empty string to store the reversed words
    result = ''
    # Iterate through the reversed words
    for i in range(len(rev)):
        # Append each word to the result string
        result += rev[i]
        # Add a space after each word, except for the last word
        if i != len(rev) - 1:
            result += ' '
    # Return the final reversed string
    return result

print(reverseWords("the sky is blue"))