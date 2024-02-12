import os
import json


class SaveLoad:

    def save(self, data):

        # Patrick : Once we have the ability to convert the Diagram to a JSON text format,
        # Patrick : this test data will be removed.
        save_folder = 'save_folder'

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            # Patrick: Checks if the save_folder already exists
            # Patrick: If not, the os will create the folder at the projects root.

        file_name = input("Enter a valid filename: ") + ".json"

        file_path = os.path.join(save_folder, file_name)

        name_exists = os.path.exists(file_path)

        print("Filename : " + file_name)
        if name_exists:
            overwrite = input(f"The file {file_name} already exists. Do you want to overwrite it? Y/N ").lower()

            if overwrite == 'y':
                print(f"Overwriting {file_name}...")

                with open(file_path, 'w') as f:
                    json.dump(data, f)
                    # Patrick: test_data will be replaced with proper diagram data once Diagram is complete

            else:
                print(f"Aborting save...")
        else:
            print(f"Saving {file_name}")
            with open(file_path, 'w') as f:
                json.dump(data, f)
                # Patrick: test_data will be replaced with proper diagram data once Diagram is complete

    def load(self, filename):

        save_folder = 'save_folder'
        # Patrick : Makes method aware of the save folder
        
        file_name = str(file_name + ".json")



        # Patrick: Prompts user to input the name of the file they would like to load
        file_path = os.path.join(save_folder, filename)
        file_exists = os.path.exists(file_path)
        if file_exists:
            # Patrick: If file exists, open the file
            with open(file_path, 'r+') as file:
                # Read the content
                content = file.read()
                print('Current Content:', content)
                file.seek(0, 2)
        else:
            # Patrick: If file does not exist, alert user
            print("File does not exist!")




