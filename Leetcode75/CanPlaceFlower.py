from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # Initialize a variable to count the number of flowers that can be planted
    count = 0
    # Create a new flowerbed with additional empty spaces at both ends
    newbed = [0] + flowerbed + [0]
    # Iterate through the new flowerbed
    for bed in range(1, len(newbed) - 1):
        # Check if the current position and its adjacent positions are all empty
        if newbed[bed - 1] == 0 and newbed[bed] == 0 and newbed[bed + 1] == 0:
            # Plant a flower at the current position
            newbed[bed] = 1
            # Increment the count of planted flowers
            count += 1
    # Check if the number of planted flowers is greater than or equal to the required amount
    return n <= count

print(canPlaceFlowers([1, 0, 0, 0, 1], 1))