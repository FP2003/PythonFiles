from typing import List

def countBits(n: int) -> List[int]:
    # Initialize a dynamic programming list with all zeros up to n+1
    dp = [0] * (n + 1)
    
    # Initialize offset variable to track powers of 2
    offset = 1

    # Iterate through numbers from 1 to n
    for i in range(1, n + 1):
        # Check if the current number is a power of 2
        if offset * 2 == i:
            offset = i  # Update the offset to the next power of 2
        # Calculate the number of set bits in the current number
        dp[i] = 1 + dp[i - offset]  
        
    return dp  # Return the list containing the count of set bits for each number

print(countBits(5))