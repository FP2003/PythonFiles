from typing import List
def largestAltitude(gain: List[int]) -> int:
    # Initialize variables to keep track of the current altitude and the maximum altitude encountered
    current = 0  # Current altitude starts at 0
    maximum = 0  # Initialize the maximum altitude encountered to 0
    # Iterate through each gain value in the list
    for i in gain:
        # Update the current altitude by adding the gain at the current step
        current += i
        # Update the maximum altitude encountered if the current altitude is greater
        maximum = max(current, maximum)
    # Return the maximum altitude encountered
    return maximum

print(largestAltitude([-5,1,5,0,-7]))