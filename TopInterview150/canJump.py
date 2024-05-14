from typing import List


def canJump(nums: List[int]) -> bool:
    # Initialize the target index to the last index of the array
    target = len(nums) - 1
    # Start iteration from the second-to-last index of the array
    i = len(nums) - 2
    
    # Iterate backwards through the array
    while i >= 0:
        # Check if it's possible to reach the current index 'i' from 'target'
        if target <= i + nums[i]:
            # If reachable, update the target index to the current index 'i'
            target = i
        # Move to the previous index
        i -= 1
    
    # If the target index reaches the beginning of the array (index 0), return True
    if target == 0:
        return True
    # If not, return False
    return False

print(canJump([2,3,1,1,4]))