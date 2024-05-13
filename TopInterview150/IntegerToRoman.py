def intToRoman(num: int) -> str:
    # List of Roman numeral symbols and their corresponding values
    listed = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
    # Initialize an empty string to store the Roman numeral representation
    ans = ''

    # Iterate through the list of Roman numeral symbols and their values in reverse order
    for symbol, value in reversed(listed):
        # Check if the current value can be divided into the given number
        if num // value:
            # Calculate the count of the current symbol
            count = num // value
            # Append the symbol to the answer string 'count' times
            ans += (count * symbol)
            # Update the number by subtracting the value multiplied by the count
            num = num % value
    
    # Return the final Roman numeral representation
    return ans


print(intToRoman(5555))