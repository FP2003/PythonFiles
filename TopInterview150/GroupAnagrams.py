from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Initialize a defaultdict to store anagrams
    solution = defaultdict(list)

    # Iterate through each word in the input list
    for word in strs:
        # Sort the characters of the word to form a key
        key = ''.join(sorted(word))
        # Append the word to the list corresponding to its key
        solution[key].append(word)

    # Return the values (lists of anagrams) from the defaultdict
    return solution.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))