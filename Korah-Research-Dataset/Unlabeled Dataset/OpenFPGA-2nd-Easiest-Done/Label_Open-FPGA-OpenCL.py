import os
import json

# Function to read the contents of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to create the dataset from a single directory
def create_dataset_from_directory(directory):
    data = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.cpp'):
                base_name = os.path.splitext(file_name)[0]
                cpp_file_path = os.path.join(root, file_name)
                h_file_path = os.path.join(root, base_name + '.h')

                cpp_content = read_file(cpp_file_path)
                data.append({"label": file_name, "data": cpp_content})

                if os.path.exists(h_file_path):
                    h_content = read_file(h_file_path)
                    data.append({"label": base_name + '.h', "data": h_content})
    return data

# Directory containing the subdirectories with .cpp and .h files
directory = '.'  # Current directory

# Create the dataset
data = create_dataset_from_directory(directory)

# Save the dataset to a JSON file
output_file = 'labeled_cpp_dataset.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Dataset saved to {output_file}")
