from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    i, j = 0, 0  # Initialize pointers
    arr = len(nums)  # Length of the array
    for l in range(arr):  # Iterate through the array
        if nums[l] == 0:  # If the current element is 0
            k -= 1  # Decrement the remaining flips
        if k < 0:  # If we've used up all flips
            if nums[i] == 0:  # If the element at the left pointer is 0
                k += 1  # Increment flips available
            i += 1  # Move left pointer to the right
    return l - i + 1  # Return the length of the longest subarray

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))