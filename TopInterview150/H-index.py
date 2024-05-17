from typing import List

def hIndex(citations: List[int]) -> int:
    # Initialize the result variable to store the h-index
    res = 0
    # Sort the citations list in ascending order
    citations.sort()
    # Reverse the sorted list to get descending order
    citations.reverse()
    
    # Iterate through the list of citations
    for i in range(len(citations)):
        # Check if the current index (i + 1) is less than or equal to the citation count at index i
        if i + 1 <= citations[i]:
            # Update the result with the current index + 1
            res = i + 1
    
    # Return the computed h-index
    return res

print(hIndex([3,0,6,1,5]))
