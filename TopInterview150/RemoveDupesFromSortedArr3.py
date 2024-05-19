from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # Check if the list is empty
    if not nums:
        return 0  # Return 0 for an empty list
    
    # Initialize the index to track the position for unique elements
    index = 2

    # Iterate through the list starting from the third element
    for i in range(2, len(nums)):
        # Check if the current element is different from the elements at positions index-1 and index-2
        if nums[i] != nums[index - 1] or nums[i] != nums[index - 2]:
            # If it's unique, assign the current element to the current index
            nums[index] = nums[i]
            # Increment the index
            index += 1
    
    # Return the length of the list with unique elements
    return index

print(removeDuplicates([1,1,1,2,2,3]))