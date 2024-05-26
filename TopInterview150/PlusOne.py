from typing import List

def plusOne(digits: List[int]) -> List[int]:
    # Iterate over the digits starting from the last one
    for i in reversed(range(len(digits))):
        # If the current digit is 9, set it to 0 (carry over)
        if digits[i] == 9:
            digits[i] = 0
        else:
            # If the current digit is not 9, increment it by 1
            digits[i] += 1
            # Return the modified list as no further carry is needed
            return digits
    # If all digits were 9, add a leading 1 to handle the carry over
    return [1] + digits
