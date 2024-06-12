from typing import List


def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)
        
