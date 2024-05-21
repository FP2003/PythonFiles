from typing import List


def jump(nums: List[int]) -> int:
    # Initialize variables
    end = 0        # The farthest point we can reach with the current number of jumps
    ans = 0        # The number of jumps needed to reach the end
    farthest = 0   # The farthest point we can reach with the next jump

    # Iterate through the list, but not including the last element
    for i in range(len(nums) - 1):
        # Update the farthest point we can reach with the current jump
        farthest = max(farthest, i + nums[i])
        
        # If the farthest point we can reach is beyond or at the last element, increment the jump count and break the loop
        if farthest >= len(nums) - 1:
            ans += 1
            break
        
        # If we have reached the end of the current jump range
        if i == end:
            # Increment the jump count
            ans += 1
            # Update the end to the farthest point we can reach with the current jump
            end = farthest
    
    # Return the total number of jumps needed to reach the end
    return ans

print(jump([2,3,1,1,4]))