from typing import List


def maxProfit(prices: List[int]) -> int:
    # Initialize the maximum profit to 0
    maxProfit = 0
    
    # Iterate through the list of prices
    for i in range(1, len(prices)):
        # If the current price is higher than the previous day's price
        if prices[i] > prices[i - 1]:
            # Add the difference to the maximum profit
            maxProfit += prices[i] - prices[i - 1]
    
    # Return the total maximum profit from multiple transactions
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))