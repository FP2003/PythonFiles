
def isHappy(n: int) -> bool:
    # Initialize current number to n
    current = n
    # Initialize variable to hold the sum of squared digits
    nums = 0
    # Dictionary to store seen numbers to detect cycles
    numbers = {}

    # Infinite loop until happy number is found or cycle detected
    while True:
        # Calculate the sum of squares of digits for the current number
        for i in str(current):
            nums += int(i) ** 2
        
        # If the sum of squares is 1, the number is happy, return True
        if nums == 1:
            return True
        # If the sum of squares is already seen, a cycle is detected, return False
        if nums in numbers:
            return False
        
        # Add the sum of squares to the dictionary to mark it as seen
        numbers[nums] = 0
        # Update the current number to the sum of squares
        current = nums
        # Reset the sum of squares for the next iteration
        nums = 0

print(isHappy(5))