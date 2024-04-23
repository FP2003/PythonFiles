def isAnagram(s: str, t: str) -> bool:
    # Convert strings to lists of characters
    s = list(s)
    t = list(t)
    
    # Sort the lists of characters
    s.sort()
    t.sort()
    
    # Check if the sorted lists are equal
    if s == t:
        # If they are equal, return True (strings are anagrams)
        return True
    else:
        # If they are not equal, return False (strings are not anagrams)
        return False
