from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    # Initialize the list to store the summary ranges
    ans = []
    # Check if the input list is empty
    if not nums:
        return ans
    # Initialize variables to track the start and end of a range
    start = end = nums[0]
    # Iterate over the numbers in the list
    for num in nums[1:]:
        # If the current number is consecutive to the previous number, extend the range
        if num == end + 1:
            end = num
        else:
            # If the current number is not consecutive, the range ends
            # Add the range to the answer list
            if start != end:
                ans.append(f"{start}->{end}")
            else:
                ans.append(str(start))
            # Reset the start and end for the new range
            start = end = num
    # Add the last range to the answer list
    if start != end:
        ans.append(f"{start}->{end}")
    else:
        ans.append(str(start))
    # Return the list of summary ranges
    return ans

print(summaryRanges([0,1,2,4,5,7]))