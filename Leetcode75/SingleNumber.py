from typing import List

def singleNumber(nums: List[int]) -> int:
    # If the list contains only one element, return that element
    if len(nums) == 1:
        return nums[0]
    
    # Iterate through the list
    for i in nums:
        # If the count of the current number is 1, it means it's a single occurrence
        if nums.count(i) == 1:
            return i  # Return the single number
