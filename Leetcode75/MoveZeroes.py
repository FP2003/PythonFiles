from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Initialize a pointer to keep track of the position where non-zero elements should be placed
    pointer = 0
        
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero
        if nums[i] != 0:
            # Swap it with the element at the pointer position
            nums[i], nums[pointer] = nums[pointer], nums[i]
            # Move the pointer to the next position
            pointer += 1
            
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)