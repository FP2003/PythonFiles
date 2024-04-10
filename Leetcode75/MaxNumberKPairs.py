from collections import Counter
from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    # Count the occurrences of each number in the list
    count_dict = Counter(nums)
    
    # Initialize the count of operations
    operations = 0
    
    # Iterate through the unique numbers in the list
    for num in count_dict:
        # Calculate the complement needed to reach the target k
        complement = k - num
        
        # Check if the complement exists in the count dictionary
        if complement in count_dict:
            # Update the count of operations with the minimum occurrences of num and its complement
            operations += min(count_dict[num], count_dict[complement])
    
    # Since each pair contributes 2 operations, divide by 2 to get the total number of pairs
    return operations // 2
