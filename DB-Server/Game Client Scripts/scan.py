import os
import re

def scan_as_files(directory, search_text):
    files_found = []
    pattern = re.compile(rf'\b{re.escape(search_text)}\b')  # Ensure exact word match
    
    print(f"Searching for: {search_text}")  # Display search text in CMD
    
    for filename in os.listdir(directory):
        if filename.endswith(".as"):  # Process only ActionScript files
            file_path = os.path.join(directory, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    if pattern.search(content):  # Search for exact match in file content
                        files_found.append(filename)
            except (UnicodeDecodeError, IOError) as e:
                print(f"Error reading {filename}: {e}")
    
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