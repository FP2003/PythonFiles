from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # Initialize a list to store the results
    res = [1] * (len(nums))
    
    # Calculate the prefix products
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]  # Update the prefix product
    
    # Calculate the postfix products and update the final result
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= post
        post *= nums[i]  # Update the postfix product
    
    return res

# Test the function
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output should be [24, 12, 8, 6]
