def mergeAlternately(word1: str, word2: str) -> str:
    # Determine which word is shorter and which is longer
    shorter, longer = (word1, word2) if len(word1) < len(word2) else (word2, word1)
    
    # Initialize an empty string to store the merged result
    merged = ""
    
    # Loop through the characters of the shorter word
    for i in range(len(shorter)):
        # Concatenate the i-th character from word1 and word2 alternately
        merged += word1[i] + word2[i] 
        
    # Append the remaining characters of the longer word to the merged result
    merged += longer[len(shorter):]
    
    # Return the merged string
    return merged

# Test the function
print(mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
