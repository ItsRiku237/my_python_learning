import os
# 4. Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  

# Ask the user for the directory path
directory = input("Enter the directory path: ")

try:
    # Get the list of files and folders in the directory
    contents = os.listdir(directory)
    
    print(f"\nContents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")
