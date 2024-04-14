from typing import List

def removeElement(nums: List[int], val: int) -> int:
    # While the value to be removed exists in the list
    while val in nums:
        # Remove the first occurrence of the value
        nums.remove(val)
        
# Test the function
print(removeElement([3,2,2,3], 3))
