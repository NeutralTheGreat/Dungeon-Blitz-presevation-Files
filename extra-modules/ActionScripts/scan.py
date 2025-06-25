import os
import re

def scan_as_files(directory, search_text):
    files_found = []
    pattern = re.compile(rf'\b{re.escape(search_text)}\b')  # Ensure exact word match

    print(f"Searching for: {search_text}")  # Display search text in CMD
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".txt"):  # Change this extension if you want .as instead
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if pattern.search(content):  # Search for exact match in file content
                            # Record the relative path from the base directory
                            rel_path = os.path.relpath(file_path, directory)
                            files_found.append(rel_path)
                except (UnicodeDecodeError, IOError) as e:
                    print(f"Error reading {file_path}: {e}")

    if files_found:
        print("Text found in:")
        for file in files_found:
            print(f"- {file}")
    else:
        print("No matches found.")

# Get search text from user input
search_text = input("Enter the word to search for: ")
directory_path = os.getcwd()  # Use current working directory
scan_as_files(directory_path, search_text)
