
def gcdOfStrings(str1: str, str2: str) -> str:
    # Importing the gcd function from the math module
    from math import gcd
        
    # If the concatenation of str1 and str2 is not equal to the concatenation of str2 and str1,
    # then there is no common divisor string that can generate both str1 and str2
    if str1 + str2 != str2 + str1:
        return ""
        
    # Calculate the greatest common divisor of the lengths of str1 and str2
    # This represents the length of the common divisor string
    # Slice str1 to get the common divisor string with length equal to the calculated gcd
    return str1[:gcd(len(str1), len(str2))]

print(gcdOfStrings("ABCABCABC", "ABC"))