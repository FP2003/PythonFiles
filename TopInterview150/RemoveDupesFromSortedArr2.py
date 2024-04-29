from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # Check if the list is empty or has only one element
    if not nums or len(nums) == 1:
        return len(nums)

    # Initialize two pointers: one for iterating through the list, 
    # and another for inserting non-duplicate elements
    slow = 1  # Start from the second position
    count = 1  # Count of current element

    # Iterate through the list starting from the second element
    for fast in range(1, len(nums)):
        # If the current element is the same as the previous one
        if nums[fast] == nums[fast - 1]:
            # Increment the count
            count += 1
        else:
            # Reset the count for the new element
            count = 1

        # If the count is less than or equal to 2, keep the element
        if count <= 2:
            nums[slow] = nums[fast]
            slow += 1

    # The length of the modified list is the position of the last non-duplicate element + 1
    return slow

print(removeDuplicates([1,1,1,2,2,3]))
