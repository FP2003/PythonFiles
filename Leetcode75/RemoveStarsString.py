def removeStars(s: str) -> str:
    # Initialize an empty list to store characters
    place = []
    # Convert the input string 's' into a list of characters
    slist = list(s)
    # Iterate through each character in the list
    for i in range(len(slist)):
        # Check if the current character is not '*'
        if slist[i] != '*':
            # If it's not '*', append it to the 'place' list
            place.append(slist[i])
        else:
            # If it's '*', remove the last character from the 'place' list
            # This simulates removing the preceding character
            place.pop()
    
    # Join the characters in the 'place' list to form a string
    # This string represents the original string without the characters following '*'
    return ''.join(place)

print(removeStars('Leet**c*ode'))