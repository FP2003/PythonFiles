def reverseVowels(s: str) -> str:
    # Define the vowels
    vowels = 'aeiouAEIOU'
    # Convert the string to a list for easy manipulation
    slist = list(s)
    # Initialize two pointers for the start and end of the string
    i = 0
    j = len(slist) - 1
    # Iterate until the pointers meet
    while i < j:
        # If the character at position i is not a vowel, move to the next character
        if slist[i] not in vowels:
            i += 1
            continue
        # If the character at position j is not a vowel, move to the previous character
        if slist[j] not in vowels:
            j -= 1
            continue
        # Swap the vowels at positions i and j
        slist[i], slist[j] = slist[j], slist[i]
        # Move the pointers towards each other
        i += 1
        j -= 1
    # Convert the list back to a string and return
    return "".join(slist)

print(reverseVowels("hello"))