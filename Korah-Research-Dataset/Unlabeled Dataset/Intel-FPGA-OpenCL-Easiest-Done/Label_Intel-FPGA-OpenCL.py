import os
import json

# Function to read the contents of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to create the dataset
def create_dataset(directory):
    data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.cpp'):
            file_path = os.path.join(directory, file_name)
            content = read_file(file_path)
            data.append({"label": file_name, "data": content})
    return data

# Directory containing the .cpp files
directory = '.'  # Current directory

# Create the dataset
data = create_dataset(directory)

# Save the dataset to a JSON file
output_file = 'labeled_cpp_dataset.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Dataset saved to {output_file}")
