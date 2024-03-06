from collections import Counter
from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    # List to store unique counts of occurrences
    unique_counts = []
    # Count the occurrences of each element in the list
    occurrence_counter = Counter(arr)
    # Iterate over the items in the Counter object
    for number, count in occurrence_counter.items():
        # Check if the count has already been encountered
        if count not in unique_counts:
            # If count is unique, add it to the list
            unique_counts.append(count)
        else:
            # If count is not unique, return False
            return False
    # If all counts are unique, return True
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))