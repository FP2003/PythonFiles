from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # Convert the list to a set for O(1) look-up times
    setter = set(nums)
    # Initialize the variable to keep track of the longest sequence
    longest = 0

    # Iterate through each number in the set
    for num in setter:
        # Check if the current number is the start of a sequence
        if (num - 1) not in setter:
            # Initialize the length of the current sequence
            length = 1
            # Continue to check for the next consecutive numbers in the sequence
            while (num + length) in setter:
                length += 1
            # Update the longest sequence length if the current sequence is longer
            longest = max(longest, length)
    
    # Return the length of the longest consecutive sequence
    return longest
