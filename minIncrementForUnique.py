from typing import List


def minIncrementForUnique(nums: List[int]) -> int:
        nums = sorted(nums)

        numTrack = 0
        minIncrement = 0

        for num in nums:
            numTrack = max(numTrack, num)
            minIncrement += numTrack - num
            numTrack += 1
        
        return minIncrement