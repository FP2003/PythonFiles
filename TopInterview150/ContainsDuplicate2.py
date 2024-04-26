from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_indices = {}

    for i, num in enumerate(nums):
        # If the number is already in the dictionary and the difference between
        # the current index and the most recent index of the number is less than or equal to k, return True
        if num in num_indices and i - num_indices[num] <= k:
            return True
        # Update the most recent index of the number
        num_indices[num] = i

    # If no such pair of duplicate elements found within k indices, return False
    return False

print(containsNearbyDuplicate([4,1,2,3,1,5], 3))