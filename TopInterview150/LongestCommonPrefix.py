from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # Check if the list is empty
    if not strs:
        return ""
    # Initialize prefix with the first string
    prefix = strs[0]
    # Iterate through the strings in the list
    for string in strs[1:]:
        # While the prefix is not a prefix of the current string
        while string.find(prefix) != 0:
            # Remove the last character from the prefix
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""
    # Return the longest common prefix
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))