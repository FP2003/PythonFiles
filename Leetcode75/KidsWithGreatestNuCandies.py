from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    # Initialize an empty list to store the results
    res = []
    # Find the maximum number of candies among all kids
    top = max(candies)
    # Iterate through each kid's candies
    for x in candies:
        # Add the extra candies to the current kid's candies
        x += extraCandies
        # Check if the total candies after adding extra candies is greater than or equal to the maximum
        if x >= top:
            # If yes, the current kid can have the maximum number of candies after adding extra candies
            res.append(True)
        else:
            # If no, the current kid can't have the maximum number of candies after adding extra candies
            res.append(False)
    # Return the list of results
    return res

# Test the function with sample inputs and print the result
print(kidsWithCandies([2,3,5,1,3], 3))
