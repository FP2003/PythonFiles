def searchInsert(nums, target):
    # Check if target is not in nums
    if target not in nums:
        # If not, append target to nums
        nums.append(target)
        # Sort the nums list
        nums.sort()
    # Return the index of the target in the sorted nums list
    return nums.index(target)

print(searchInsert([1,3,5,6],5))