
import os
import json

fileName = input("Enter a valid filename: ")
# Name checker goes here
name_exists = True  # This will be replaced with os.path.exists(fileName). This is in place, so we can easily test.

print("Filename : " + fileName)
if name_exists:
    overwrite = input(f"The file {fileName} already exists. Do you want to overwrite it? Y/N ")

    if overwrite == 'Y' or overwrite == 'y':
        print(f"Overwriting {fileName}...")
        # Save logic
    else:
        print(f"Not overwriting {fileName}, exiting... ")
else:
    print(f"Saving {fileName}")
    # Save logic
