# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n: int) -> int:
    # Initialize variables to represent the leftmost and rightmost boundaries of the search range
    left, right = 1, n
    # Run a binary search loop until the correct number is found
    while True:
        # Calculate the middle number of the current search range
        mid = (left + right) // 2
        # Use the 'guess' function to determine whether the guessed number is too high, too low, or correct
        result = guess(mid)
        # If the guessed number is too high, adjust the search range by setting 'right' to one less than the guessed number
        if result > 0:
            left = mid + 1
        # If the guessed number is too low, adjust the search range by setting 'left' to one more than the guessed number
        elif result < 0:
            right = mid - 1
        # If the guessed number is correct, return the guessed number
        else:
            return mid

# Will not show result due to no API for guess function.