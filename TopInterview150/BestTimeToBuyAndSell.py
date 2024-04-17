from typing import List

def maxProfit(prices: List[int]) -> int:
    # Initialize variables to track maximum profit and minimum price
    profit = 0
    minimum = prices[0]
    
    # Iterate through the prices
    for i in range(len(prices)):
        # Update the minimum price if the current price is lower
        if prices[i] < minimum:
            minimum = prices[i]
        
        # Calculate the profit by selling at the current price
        # and buying at the minimum price seen so far
        profit = max(profit, prices[i] - minimum)
    
    # Return the maximum profit
    return profit
