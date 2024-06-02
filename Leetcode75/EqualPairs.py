from collections import defaultdict
from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    # Initialize a dictionary to store the count of each row's string representation
    hashMap = defaultdict(int)
    # Initialize a counter for the number of equal row-column pairs
    count = 0

    # Convert each row to a string and count its occurrences
    for row in grid:
        hashMap[str(row)] += 1

    # Iterate over each column index
    for i in range(len(grid[0])):
        # Initialize a list to store the current column elements
        columns = []
        # Collect the elements of the current column
        for j in range(len(grid)):
            columns.append(grid[j][i])
        # Convert the column to a string and add its count from hashMap to the total count
        count += hashMap[str(columns)]
    
    # Return the total number of equal row-column pairs
    return count
