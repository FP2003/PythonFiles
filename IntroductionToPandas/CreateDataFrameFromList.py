import pandas as pd
from typing import List

# Function to create a pandas DataFrame from student data
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create DataFrame from student_data with specified column names
    table = pd.DataFrame(student_data, columns=('student_id', 'age'))
    return table

# Sample student data
student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]

# Create DataFrame from student_data and print it
print(createDataframe(student_data))
