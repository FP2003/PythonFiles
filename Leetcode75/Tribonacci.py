# Function to calculate the nth tribonacci number
def tribonacci(n: int) -> int:
    # Helper function to calculate fibonacci number recursively
    def fib(n):
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        # If the value is already computed, return it
        elif dp[n] != -1:
            return dp[n]
        # Calculate the tribonacci number recursively
        dp[n] = fib(n - 1) + fib(n - 2) + fib(n - 3)
        return dp[n]

    # Initialize the dynamic programming array with -1
    dp = [-1] * (n + 1)
    # Calculate the nth tribonacci number
    a = fib(n)
    return a
