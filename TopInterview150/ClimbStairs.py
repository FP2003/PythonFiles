def climbStairs(n: int) -> int:
    # If there are 0 or 1 steps, there's only one way to climb (trivially return 1)
    if n == 0 or n == 1:
        return 1

    # Initialize the first two steps, where there's 1 way to stay at the ground (0 steps) 
    # and 1 way to reach the first step (1 step)
    previous = 1
    current = 1

    # Iterate from the second step to the nth step
    for i in range(2, n + 1):
        # The number of ways to reach the current step is the sum of the ways to reach
        # the previous step and the step before that
        current = previous + current
        # Update the previous step to be the current step before the update
        previous = current - previous

    # Return the total number of ways to reach the nth step
    return current
