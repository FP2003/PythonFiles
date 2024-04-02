from typing import List


def pivotIndex(nums: List[int]) -> int:
    # Initialize leftSum to 0 to keep track of the running sum of elements to the left of the current index
    leftSum = 0
    # Calculate the total sum of all elements in the array
    total = sum(nums)
    
    # Iterate through the array using enumerate to also get the index of each element
    for i, num in enumerate(nums):
        # Check if the sum of elements to the left of the current index is equal to the sum of elements to the right
        if leftSum == (total - leftSum - num):
            return i  # If equal, return the current index as the pivot index
        leftSum += num  # Update the leftSum by adding the current element
        
    # If no pivot index is found, return -1
    return -1

print(pivotIndex([1,7,3,6,5,6]))