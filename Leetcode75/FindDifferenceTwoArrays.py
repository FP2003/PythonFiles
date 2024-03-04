from typing import List
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    # Initialize an empty list to store the result
    res = []
    # Find elements that are in nums1 but not in nums2
    diff1 = list(set(nums1) - set(nums2))
    # Find elements that are in nums2 but not in nums1
    diff2 = list(set(nums2) - set(nums1))
    # Append the differences to the result list
    res.append(diff1)
    res.append(diff2)
    # Return the result
    return res

print(findDifference([1,2,3], [2,4,6]))