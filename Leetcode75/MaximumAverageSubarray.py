from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
        # Initialize sum variable
        summ = 0
        # Calculate sum of first 'k' elements
        for i in range(k):
            summ += nums[i]
        # Initialize maxSum variable with sum of first 'k' elements
        maxSum = summ
        # Initialize start and end indices
        sindex = 0
        eindex = k
        # Iterate through the list to find maximum sum
        while eindex < len(nums):
            # Remove the first element of the current subarray from the sum
            summ -= nums[sindex]
            sindex += 1
            # Add the next element to the sum
            summ += nums[eindex]
            eindex += 1
            # Update maxSum if necessary
            maxSum = max(maxSum, summ)
        # Return the maximum average
        return maxSum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))