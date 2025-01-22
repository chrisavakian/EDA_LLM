import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to read the contents of a file
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return ""

# Function to create the dataset from a single directory
def create_dataset_from_directory(directory):
    data = []
    source_extensions = ('.c', '.cpp', '.cxx', '.cc', '.C', '.tcc', '.txx', '.ipp')
    header_extensions = ('.h', '.hpp', '.hh', '.hxx', '.inl', '.inline')

    # os.walk recursively traverses the directory tree
    for root, dirs, files in os.walk(directory):
        logging.info(f"Traversing directory: {root}")
        for file_name in files:
            if file_name.endswith(source_extensions):
                base_name = os.path.splitext(file_name)[0]
                source_file_path = os.path.join(root, file_name)
                source_content = read_file(source_file_path)
                data.append({"label": file_name, "data": source_content})
                logging.info(f"Processed source file: {source_file_path}")

                for header_extension in header_extensions:
                    header_file_path = os.path.join(root, base_name + header_extension)
                    if os.path.exists(header_file_path):
                        header_content = read_file(header_file_path)
                        data.append({"label": os.path.basename(header_file_path), "data": header_content})
                        logging.info(f"Processed header file: {header_file_path}")
    return data

# Directory containing the subdirectories with source and header files
directory = '.'  # Current directory

# Create the dataset
data = create_dataset_from_directory(directory)

# Save the dataset to a JSON file
output_file = 'labeled_cpp_dataset.json'
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

logging.info(f"Dataset saved to {output_file}")
logging.info(f"Total number of files processed: {len(data)}")

# Check the total size of the data
total_size = sum(len(item["data"]) for item in data)
logging.info(f"Total size of data in JSON: {total_size} bytes")
