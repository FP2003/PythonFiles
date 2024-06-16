def isIsomorphic(s: str, t: str) -> bool:
    # Initialize arrays to store the last seen index of each character
    indexS = [0] * 200
    indexT = [0] * 200

    # If the lengths of the strings are not equal, they cannot be isomorphic
    if len(s) != len(t):
        return False

    # Iterate through the characters of the strings
    for i in range(len(s)):
        # If the last seen indices of the current characters do not match, return False
        if indexS[ord(s[i])] != indexT[ord(t[i])]:
            return False

        # Update the last seen index for the current characters in both strings
        indexS[ord(s[i])] = i + 1
        indexT[ord(t[i])] = i + 1

    # If all checks pass, the strings are isomorphic
    return True
