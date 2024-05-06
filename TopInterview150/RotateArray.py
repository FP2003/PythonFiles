from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Rotate the list k times
    for i in range(k):
        n = nums.pop()
        nums.insert(0, n)

print(rotate([1,2,3,4,5,6,7], 3))