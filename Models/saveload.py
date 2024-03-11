import os
import json
from jsonschema import validate


class SaveLoad:

    def save(self, data, file_name):
        """
            Save data to a .json file in a folder 'saves_folder'
            :param data : The data to be saved into the .json file.
            :param file_name: The name of the file the user would like to save.

            Preconditions:
            'file_name' must be a valid file name.

            Post-Conditions:
            If saves_folder did not exist, it is created.
            a .json file named 'file_name' will be within saves_folder

            Raises:
            File Overwrite
            Invalid file name



        """
        save_folder = 'save_folder'

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            # Patrick: Checks if the save_folder already exists
            # Patrick: If not, the os will create the folder at the projects root.

        file_name = str(file_name + ".json")

        file_path = os.path.join(save_folder, file_name)

        name_exists = os.path.exists(file_path)

        if name_exists:
            overwrite = input(f"The file '{file_name}' already exists. Do you want to overwrite it? Y/N ").lower()

            if overwrite == 'y':
                print(f"Overwriting '{file_name}'...")

        with open(file_path, 'w') as f:
            # Ensure json.dump() uses the indent parameter for nicely formatted JSON
            json.dump(data, f, indent=2)

        if name_exists and overwrite != 'y':
            print(f"Aborting save...")
        else:
            print(f"Saving '{file_name}'")
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
                
           
    def load(self, file_name):
        """
        Load a .json file from 'saves_folder' to be viewed/edited.

        :param file_name: The name of the file to be loaded.
        :return data: the loaded data from the desired .json file.

        Pre-conditions:
        'file_name' must be a valid file name
        'file_name' must exist in saves_folder

        Post-Conditions:
        'file_name' is loaded and the current data is printed.
        data is returned.

        """
        save_folder = 'save_folder'
        # Patrick : Makes method aware of the save folder
        
        file_name = str(file_name + ".json")

        file_path = os.path.join(save_folder, file_name)
        file_exists = os.path.exists(file_path)
        if file_exists:
            schema_path = os.path.join(save_folder, "umlSchema.json")
            schema_exists= os.path.exists(schema_path)
            if schema_exists:
                with open(schema_path, 'r') as schema_file:
                    schema = json.load(schema_file)
                # Patrick: If file exists, open the file
                    with open(file_path, 'r+') as file:
                        # Read the content
                        data = json.load(file)
                        try:
                            # Validate data against schema
                            validate(instance=data, schema=schema)
                            return data
                        except Exception as e:
                            raise ValueError("JSON data is not valid:", e)

                
        else:
            # Patrick: If file does not exist, alert user
            raise ValueError ("File does not exist!")





