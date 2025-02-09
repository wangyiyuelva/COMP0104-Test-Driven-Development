import pandas as pd
import ast
import csv

def is_java_file(filename):
    return filename.endswith('.java')

def is_test_file(filename):
    return (filename.startswith('Test') and filename.endswith('.java')) or filename.endswith('Test.java')

# Path to the CSV file generated by PyDriller
csv_path = './pydrillerData/ignite.csv'  # Replace with your CSV file path

# Read the CSV file
df = pd.read_csv(csv_path)

# Initialize lists to store the counts
java_files_count = 0
test_files_count = 0
# Process each row in the DataFrame
for index, row in df.iterrows():
    try:
        modified_files = ast.literal_eval(row['modified_file'])
    except ValueError:
        # Skip row if parsing fails
        continue



    for file in modified_files:
        if len(file) > 1 and file[1] == 'ADD':
            if is_java_file(file[0]):
                java_files_count += 1
            if is_test_file(file[0]):
                test_files_count += 1


print(f"Number of Java files: {java_files_count}")
print(f"Number of Java Test files: {test_files_count}")
