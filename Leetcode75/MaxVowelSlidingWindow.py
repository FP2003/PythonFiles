def maxVowels(s: str, k: int) -> int:
    vowels = 'aeiou'  # String containing vowels
    
    if len(s) == 0 or k <= 0:
        return 0
    
    curr_vowel = 0  # Counter for vowels in the current window
    max_vowels = 0  # Maximum number of vowels found in any window
    left, right = 0, 0  # Pointers for the sliding window
    
    # Iterate through the string using a sliding window approach
    while right < len(s):
        # If the current character is a vowel, increment the vowel count
        if s[right] in vowels:
            curr_vowel += 1
        
        # If the window size is greater than k, move the left pointer to shrink the window
        if right - left + 1 > k:
            # If the character going out of the window is a vowel, decrement the vowel count
            if s[left] in vowels:
                curr_vowel -= 1
            left += 1
        
        # Update the maximum number of vowels encountered so far
        max_vowels = max(max_vowels, curr_vowel)
        
        # Move the right pointer to expand the window further
        right += 1
    
    return max_vowels
