def trailingZeroes(n: int) -> int:
    # Initialize the count of trailing zeroes
    count = 0

    # Loop to count factors of 5 in the numbers from 1 to n
    while n > 0:
        # Divide n by 5 to count how many multiples of 5 are there
        n //= 5
        # Add the result to the count (this includes multiples of 25, 125, etc.)
        count += n
    
    # Return the total count of trailing zeroes in n!
    return count


print(trailingZeroes(5))