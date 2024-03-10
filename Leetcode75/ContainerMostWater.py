from typing import List
def maxArea(height: List[int]) -> int:
    # Initialize pointers for the left and right ends of the container
    left, right = 0, len(height) - 1
    # Initialize a variable to store the maximum area
    result = 0
    # Continue the loop until the left pointer is less than the right pointer
    while left < right:
        # Calculate the area of the current container
        area = (right - left) * min(height[left], height[right])
        
        # Update the maximum area if the current area is greater
        result = max(result, area)

        # Move the pointer that corresponds to the shorter height towards the other pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    # Return the maximum area found
    return result

print(maxArea([1,8,6,2,5,4,8,3,7]))