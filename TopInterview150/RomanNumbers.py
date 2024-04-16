def romanToInt(s: str) -> int:
    # Dictionary to map Roman numerals to their integer values
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the answer
    ans = 0
    
    # Iterate through each character of the string, except for the last one
    for i in range(len(s) - 1):
        # If the current numeral is smaller than the next one, subtract its value from the answer
        if roman[s[i]] < roman[s[i+1]]:
            ans -= roman[s[i]]
        # Otherwise, add its value to the answer
        else:
            ans += roman[s[i]]
    
    # Add the value of the last character to the answer
    return ans + roman[s[-1]]

print(romanToInt('III'))