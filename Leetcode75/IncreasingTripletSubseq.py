from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    # Initialize two variables to store the smallest and second smallest numbers
    first = float('inf')
    second = float('inf')
    
    # Iterate through the list of numbers
    for i in nums:
        # If the current number is less than or equal to the smallest number seen so far
        if i <= first:
            first = i  # Update the smallest number
        # If the current number is greater than the smallest but less than or equal to the second smallest
        elif i <= second:
            second = i  # Update the second smallest number
        # If the current number is greater than both smallest and second smallest, we found an increasing triplet
        else:
            return True
    
    # If no increasing triplet is found after iterating through the list, return False
    return False

print(increasingTriplet([1,2,3,4,5]))