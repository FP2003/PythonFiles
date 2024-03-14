from typing import List  # Importing List type for type hinting


def asteroidCollision(asteroids: List[int]) -> List[int]:
    res = []  # Initialize an empty list to store remaining asteroids after collisions
    for i in asteroids:  # Iterate through each asteroid in the input list
        while res and i < 0 and res[-1] > 0:  # Check for possible collision conditions
            difference = i + res[-1]  # Calculate the difference in sizes of colliding asteroids
            if difference < 0:  # If the current asteroid is destroyed
                    res.pop()  # Remove the larger asteroid from the list
            elif difference > 0:  # If the current asteroid survives
                i = 0  # Set the current asteroid size to 0, indicating destruction
            else:  # If both asteroids are destroyed
                i = 0  # Set the current asteroid size to 0
                res.pop()  # Remove the larger asteroid from the list
        if i:  # If the current asteroid survives without collision
            res.append(i)  # Add the current asteroid to the result list
    return res  # Return the list of remaining asteroids after collisions

print(asteroidCollision([10,2,-5]))