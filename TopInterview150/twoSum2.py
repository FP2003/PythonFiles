from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    # Initialize two pointers, i starting at the beginning and j at the end of the list
    i = 0
    j = len(numbers) - 1

    # Continue the loop until the two pointers meet
    while i < j:
        # Calculate the sum of the numbers at the current pointers
        current_sum = numbers[i] + numbers[j]
        
        # Check if the current sum matches the target
        if current_sum == target:
            # If the target is found, return the 1-based indices of the two numbers
            return [i + 1, j + 1]
        # If the current sum is less than the target, increment the left pointer i
        elif current_sum < target:
            i += 1
        # If the current sum is greater than the target, decrement the right pointer j
        else:
            j -= 1
    
    # If no valid pair is found, return an empty list
    return []
